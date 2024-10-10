from  datetime import datetime, timedelta

from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator

# ------------------- TASK FUNCTION START -------------------
def hello_world():
    return "Hello, Airflow!"

# ------------------- TASK FUNCTION END -------------------

default_args = {
    'owner' : 'asma-chloe.farah@afiniti.com',

    'retries': 3,  # Retry up to 3 times
    'retry_delay': timedelta(minutes=1),  # Wait 1 minutes between retries,

    'email_on_failure' : False,
    'email_on_retry' : False,
    
    'email' : ["noreply@astronomer.io", "noreply2@astronomer.io"],
}


with DAG(
    #Mandatory params
    dag_id = "1_my_first_dag", #Should be unique
    start_date=datetime(2024, 10, 1),
    schedule='@once', #https://airflow.apache.org/docs/apache-airflow/1.10.1/scheduler.html#dag-runs

    #Optionnal params but I usually put it
    description="ETL DAG", 
    tags=["example"],
    is_paused_upon_creation=True,
    catchup=False,

    default_args = default_args,
) as dag:
    
    # Define the tasks
    task_1 = PythonOperator(
        task_id='say_hello',
        python_callable=hello_world
    )

    task_1  # This will execute the single task