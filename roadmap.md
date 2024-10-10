# GOAL
- Understand airflow
- Commonly used operators for building data pipelines

# Understand airflow and basic
## 1_my_first_dag
**DAG** : 1_my_first_dag

**GOAL** :
- Understand the structure of a DAG, tasks
- Introduce PythonOperator for executing Python code.

## 2_etl_postgres_operator_dag (Basic ETL Process with DB Operators)
**DAG** : 2_etl_postgres_operator_dag

**GOAL** :
- Learn how to set dependencies between tasks.
- Check logs for errors in Airflow UI
- Learn how to connect to a PostgreSQL database using the PostgresOperator.
- Showcase how to execute SQL statements as part of the workflow.
- Dependencies on external DAGs using TriggerDagRunOperator 

## 3_etl_python_operators_dag
**DAG**: 3_etl_python_operators_dag
**GOAL** :
- Demonstrate the extraction of data from PostgreSQL using `PostgresHook`.
- Showcase the use of `PythonOperator` to perform data transformation.
- Write the transformed data to a CSV file.
- Showcase intertask communication.

## 4_file_dependent_branching_dag
**DAG**: 4_file_dependent_branching_dag
**GOAL** :
- Demonstrate how to use `BranchPythonOperator` for conditional task execution.
- Learn about how to use `DummyOperator` for testing or clean DAG endings.

# What's next ?

## Run DBT models
DBT models can run with `BashPythonOperator` [see example here](https://rasiksuhail.medium.com/orchestrating-dbt-with-airflow-a-step-by-step-guide-to-automating-data-pipelines-part-i-7a6db8ebc974)

## Data validation
There are many ways to ensure data quality :
- Through DBT with DBT Test
- Through external libraries like great expectations that adds new operators to Airflow.