from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 5, 28),  # ✅ Updated to today's date
    'depends_on_past': False,
    'email': ['vishal.bulbule@techtrapture.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    dag_id='fetch_cricket_stats',
    default_args=default_args,
    description='Runs an external Python script',
    schedule_interval='@daily',
    catchup=False,
    tags=['example'],
)

run_script_task = BashOperator(
    task_id='run_script',
    bash_command='python /home/airflow/gcs/dags/scripts/extract_and_push_data_gcs.py',
    dag=dag,
)
