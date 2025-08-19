from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def greet():
    print("􀀀 Hello, Airflow is running!")
with DAG(
    dag_id="hello_dag",
    start_date=datetime(2023, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    hello = PythonOperator(
        task_id="greet_task",
        python_callable=greet
)