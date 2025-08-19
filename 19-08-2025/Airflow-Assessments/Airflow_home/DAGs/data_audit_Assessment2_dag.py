import json
import logging
from datetime import datetime, timedelta
from random import randint
from airflow import DAG
from airflow.exceptions import AirflowException
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from __future__ import annotations

AUDIT_OUTPUT_PATH = "/tmp/audit_result.json"
THRESHOLD = 750    
STALE_MINUTES = 20     

def pull_external_data(**context):
    """
    Simulate reading data from an external API/DB.
    Produces a dict with a numeric metric and a timestamp.
    """
    logger = logging.getLogger("airflow.task")
   
    payload = {
        "source": "dummy_api",
        "metric_value": randint(500, 1000), 
        "pulled_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
    }
    logger.info("Pulled external data: %s", payload)
   
    context["ti"].xcom_push(key="payload", value=payload)


def validate_business_rules(**context):
    """
    Validate two rules:
      1) metric_value >= THRESHOLD
      2) pulled_at is not stale by more than STALE_MINUTES
    Always writes /tmp/audit_result.json before success/fail.
    Raises AirflowException on validation failure to fail cleanly.
    """
    logger = logging.getLogger("airflow.task")

    payload = context["ti"].xcom_pull(key="payload", task_ids="data_pull")
    if not payload:
        raise AirflowException("No payload found from data_pull task.")

    pulled_at = datetime.fromisoformat(payload["pulled_at"].replace("Z", ""))
    age_minutes = (datetime.utcnow() - pulled_at).total_seconds() / 60.0

    metric_ok = payload["metric_value"] >= THRESHOLD
    freshness_ok = age_minutes <= STALE_MINUTES

    status = "SUCCESS" if (metric_ok and freshness_ok) else "FAILURE"
    details = []

    if not metric_ok:
        details.append(
            f"metric_value {payload['metric_value']} < threshold {THRESHOLD}"
        )
    if not freshness_ok:
        details.append(
            f"data stale by {age_minutes:.1f} min (> {STALE_MINUTES} min)"
        )

    result = {
        "status": status,
        "source": payload["source"],
        "metric_value": payload["metric_value"],
        "threshold": THRESHOLD,
        "pulled_at": payload["pulled_at"],
        "age_minutes": round(age_minutes, 2),
        "details": details or ["All rules passed"],
        "validated_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
    }

    with open(AUDIT_OUTPUT_PATH, "w") as f:
        json.dump(result, f, indent=2)

    if status == "FAILURE":
        logger.error("AUDIT FAILED: %s", result)

        raise AirflowException("Audit validation failed; see audit_result.json")
    else:
        logger.info("AUDIT PASSED: %s", result)


def final_status_update(**context):
    """
    Read the audit_result.json and log a friendly final status update.
    """
    logger = logging.getLogger("airflow.task")
    with open(AUDIT_OUTPUT_PATH, "r") as f:
        result = json.load(f)

    if result["status"] == "SUCCESS":
        logger.info(
            "FINAL STATUS: Audit SUCCESS (metric=%s, threshold=%s, age=%s min)",
            result["metric_value"],
            result["threshold"],
            result["age_minutes"],
        )
    else:
        logger.warning(
            "FINAL STATUS: Audit FAILURE — %s",
            "; ".join(result.get("details", [])),
        )

default_args = {
    "owner": "karthika",              
    "email": ["alerts@example.com"],     
    "email_on_failure": True,
    "email_on_retry": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="data_audit_dag",              
    description="Scheduled data audit with rule validation and final status",
    default_args=default_args,
    start_date=datetime(2025, 8, 1),
    schedule_interval="@hourly",         
    catchup=False,
    tags=["audit", "event-driven", "example"],
) as dag:

    data_pull = PythonOperator(
        task_id="data_pull",
        python_callable=pull_external_data,
        provide_context=True,
    )

    audit_validate = PythonOperator(
        task_id="audit_rule_validation",
        python_callable=validate_business_rules,
        provide_context=True,
    )

    log_results = BashOperator(
        task_id="logging_audit_results",
        bash_command=(
            f"echo '--- AUDIT RESULTS ---' && "
            f"cat {AUDIT_OUTPUT_PATH} && "
            f"echo && echo 'Custom Log: Audit processing complete.'"
        ),
    )

    final_update = PythonOperator(
        task_id="final_status_update",
        python_callable=final_status_update,
        provide_context=True,
    )

    data_pull >> audit_validate >> log_results >> final_update
