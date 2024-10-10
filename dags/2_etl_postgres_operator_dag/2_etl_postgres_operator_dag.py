from  datetime import datetime, timedelta

from airflow.models.dag import DAG
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.dagrun_operator import TriggerDagRunOperator

default_args = {
    'owner' : 'asma-chloe.farah@afiniti.com',

    'email_on_failure' : False,
    'email_on_retry' : False,
    
    'email' : ["asma-chloe.farah@afiniti.com", "anotheremail@afiniti.com"],
}


with DAG(
    dag_id = "2_etl_postgres_operator_dag",
    start_date=datetime(2024, 10, 1),
    schedule='@once',
    description="This small example mimics the steps of an ETL process", 
    tags=["example"],
    is_paused_upon_creation=True,
    catchup=False,
    default_args = default_args,
) as dag:
    
    create_table = PostgresOperator(
        task_id='create_table',
        postgres_conn_id='postgres',
        sql="""
            CREATE TABLE IF NOT EXISTS public.orders (
                order_id SERIAL PRIMARY KEY,
                product_name VARCHAR(255) NOT NULL,
                quantity INT NOT NULL,
                price NUMERIC(10, 2) NOT NULL,
                order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """
    )

    seed_table = PostgresOperator(
        task_id='seed_table',
        postgres_conn_id='postgres',
        sql="seed_table.sql"
    )

    trigger_dag_3 = TriggerDagRunOperator(
        task_id='trigger_dag_3',
        trigger_dag_id='3_etl_python_operators_dag'
    )
    
    create_table >> seed_table >> trigger_dag_3