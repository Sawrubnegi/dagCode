from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import os
import shutil

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 30),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'move_txt_file',
    default_args=default_args,
    description='Move .txt file to another folder',
    schedule_interval=timedelta(hours=1),
)

def move_file(src_folder, dst_folder, **kwargs):
    for filename in os.listdir(src_folder):
        if filename.endswith(".txt"):
            shutil.move(os.path.join(src_folder, filename), dst_folder)

move_file_task = PythonOperator(
    task_id='move_file',
    python_callable=move_file,
    op_args=['/path/to/src/folder', '/path/to/dst/folder'],
    dag=dag,
)

