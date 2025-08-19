from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract_data(**kwargs):
    data = "id,name,sales\n1,Alice,300\n2,Bob,450\n3,Charlie,500"
    with open("/tmp/extracted_data.csv", "w") as f:
        f.write(data)
    print("Data Extracted and stored at /tmp/extracted_data.csv")

def transform_data(**kwargs):
    input_path = "/tmp/extracted_data.csv"
    output_path = "/tmp/transformed_data.csv"

    with open(input_path, "r") as infile, open(output_path, "w") as outfile:
        lines = infile.readlines()
        header = lines[0].strip() + ",bonus\n"
        outfile.write(header)
        for row in lines[1:]:
            id, name, sales = row.strip().split(",")
            bonus = int(sales) * 0.1
            outfile.write(f"{id},{name},{sales},{bonus}\n")
    print("Data Transformed and saved at /tmp/transformed_data.csv")

def load_data(**kwargs):
    with open("/tmp/transformed_data.csv", "r") as f:
        content = f.read()
    print("Loaded data:\n", content)

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2025, 8, 1),
    "retries": 1,
}

with DAG(
    dag_id="etl_pipeline_dag",
    default_args=default_args,
    description="A simple ETL pipeline using Airflow",
    schedule_interval=None,  # manually trigger
    catchup=False,
    tags=["ETL", "example"],
) as dag:

    extract_task = PythonOperator(
        task_id="extract",
        python_callable=extract_data,
    )

    transform_task = PythonOperator(
        task_id="transform",
        python_callable=transform_data,
    )

    load_task = PythonOperator(
        task_id="load",
        python_callable=load_data,
    )

    notify = BashOperator(
        task_id="notify",
        bash_command="echo 'ETL Pipeline Completed Successfully!'"
    )

    extract_task >> transform_task >> load_task >> notify
