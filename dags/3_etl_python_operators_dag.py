from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.postgres_hook import PostgresHook
import csv

def extract_data_from_postgres():
    postgres_hook = PostgresHook(postgres_conn_id='postgres')
    orders_df = postgres_hook.get_pandas_df("SELECT order_id, product_name, quantity, price, order_date FROM public.orders")
    return orders_df

def write_to_csv(**context):
    orders = context['ti'].xcom_pull(task_ids='extract_orders_data')

    file_path = '/tmp/orders.csv'
    with open(file_path, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['order_id', 'product_name', 'quantity', 'price', 'order_date'])
        writer.writerows(orders)
    print(f"Orders data written to {file_path}")
    return file_path
    
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
    dag_id="3_etl_python_operators_dag",
    start_date=datetime(2024, 10, 1),
    schedule_interval=None,
    description="This small example mimics the steps of an ETL process using only PythonOperators and showcase inter-task communication",
    catchup=False,
    is_paused_upon_creation=False,
    default_args=default_args,
) as dag:
    
    extract_task = PythonOperator(
        task_id='extract_orders_data',
        python_callable=extract_data_from_postgres
    )
    
    write_to_csv_task = PythonOperator(
        task_id='write_orders_to_csv',
        python_callable=write_to_csv,
        provide_context=True
    )
    
    extract_task >> write_to_csv_task
