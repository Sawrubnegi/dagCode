import boto3
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import os

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
    'move_txt_file_to_s3',
    default_args=default_args,
    description='Move .txt file to AWS S3',
    schedule_interval=timedelta(hours=1),
)

def move_file_to_s3(src_folder, s3_bucket, s3_key, **kwargs):
    s3 = boto3.client('s3')
    for filename in os.listdir(src_folder):
        if filename.endswith(".txt"):
            s3.upload_file(os.path.join(src_folder, filename), s3_bucket, s3_key + filename)

move_file_to_s3_task = PythonOperator(
    task_id='move_file_to_s3',
    python_callable=move_file_to_s3,
    op_args=['/path/to/src/folder', 'my-s3-bucket', 'path/to/s3/key/'],
    dag=dag,
)
