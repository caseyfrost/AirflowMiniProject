from datetime import timedelta
from pathlib import Path
from airflow import DAG
from airflow.operators.python import PythonOperator

# The folder where airflow should store its log files
# This path must be absolute
# marketvol log directory
log_dir = r'/Users/caseyfrost/airflow/logs/marketvol'


def analyze_file(file):
    error_count = 0
    error_messages = []
    with open(file, 'r') as f:
        for line in f.readlines():
            if 'ERROR' in line:
                error_count += 1
                error_messages.append(line)
    return error_count, error_messages


def main(logs):
    file_list = Path(logs).rglob('*.log')
    errors = []
    for file in file_list:
        count, cur_list = analyze_file(file)
        if len(cur_list) > 0:
            for error in cur_list:
                errors.append(error.strip('\n'))
    print(f'Total errors: {len(errors)}')
    for error in errors:
        print(error)


default_args = {
    'owner': 'cfrost',
    'start_date': '2022-4-22',
    'end_date': '2022-5-1',
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    dag_id='error_logs',
    default_args=default_args,
    description='Sum count of error logs and print error messages',
    schedule_interval='@once',
)

t0 = PythonOperator(
    task_id='error_report',
    dag=dag,
    python_callable=main,
    op_kwargs={'logs': log_dir}
)
