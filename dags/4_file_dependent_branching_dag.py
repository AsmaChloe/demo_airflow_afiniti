from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import BranchPythonOperator, PythonOperator
from airflow.operators.dummy_operator import DummyOperator
import os


def check_file():
    file_path = '/tmp/orders.csv'
    if os.path.exists(file_path):
        return 'process_file_task'
    else:
        return 'no_file_task'

def process_file():
    file_path = '/tmp/orders.csv'
    with open(file_path, 'r') as file:
        orders = file.readlines()
    print(f"Processing {len(orders) - 1} orders from the file.")

# Define default arguments
default_args = {
    'owner': 'asma-chloe.farah@afiniti.com',
    'retries': 3,
    'retry_delay': timedelta(minutes=1),
    'email_on_failure': False,
    'email_on_retry': False,
    'email': ["asma-chloe.farah@afiniti.com", "anotheremail@afiniti.com"],
}

# Define the DAG
with DAG(
    dag_id="4_file_dependent_branching_dag",
    start_date=datetime(2024, 10, 1),
    schedule_interval="@once",
    description="Branching DAG based on data validation in Postgres",
    catchup=False,
    default_args=default_args,
) as dag:
    
    branch_task = BranchPythonOperator(
        task_id='branch_task',
        python_callable=check_file
    )

    process_file_task = PythonOperator(
        task_id='process_file_task',
        python_callable=process_file
    )

    no_file_task = DummyOperator(
        task_id='no_file_task'
    )


    branch_task >> [process_file_task, no_file_task]