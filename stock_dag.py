import yfinance as yf
import pandas as pd
from airflow import DAG
from datetime import timedelta, date
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

cur_date = date.today()

default_args = {
    'owner': 'cfrost',
    'start_date': '2022-4-22',
    'end_date': '2022-5-1',
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

temp_dir = f'/Users/caseyfrost/Desktop/Springboard/AirFlow/temp/data/{cur_date}'
data_lake = r'/Users/caseyfrost/Desktop/Springboard/AirFlow/Stock_Extracts'


def get_stock_data(start_date, symbol):
    end_date = start_date + timedelta(days=1)
    df = yf.download(symbol, start=start_date, end=end_date, interval='1m')
    df.to_csv(f'{temp_dir}/{symbol}.csv', header=False)


def query(data_loc, today_date):
    df = pd.read_csv(f'{data_loc}/AAPL_{today_date}.csv')
    print('AAPL Dataframe Head:')
    print(df.head())
    print('----------------')
    print('AAPL Count:')
    print(len(df))
    print('----------------')
    print('AAPL Total Volume:')
    print(df['Volume'].sum())

    print('----------------')
    df = pd.read_csv(f'{data_loc}/TSLA_{today_date}.csv')
    print('TSLA Dataframe Head:')
    print(df.head())
    print('----------------')
    print('TSLA Count:')
    print(len(df))
    print('----------------')
    print('TSLA Total Volume:')
    print(df['Volume'].sum())


dag = DAG(
    dag_id='marketvol',
    default_args=default_args,
    description='A simple DAG',
    schedule_interval='0 18 * * 1-5'
)

t0 = BashOperator(
    task_id='Create_Temp_Dir',
    dag=dag,
    bash_command=f'mkdir -p {temp_dir}'
)

t1 = PythonOperator(
    task_id='AAPL_Download',
    dag=dag,
    python_callable=get_stock_data,
    op_kwargs={'start_date': cur_date, 'symbol': 'AAPL'}
)

t2 = PythonOperator(
    task_id='TSLA',
    dag=dag,
    python_callable=get_stock_data,
    op_kwargs={'start_date': cur_date, 'symbol': 'TSLA'}
)

t3 = BashOperator(
    task_id='move_aapl',
    dag=dag,
    bash_command=f'mv {temp_dir}/AAPL.csv {data_lake}/AAPL_{cur_date}.csv'
)

t4 = BashOperator(
    task_id='move_tsla',
    dag=dag,
    bash_command=f'mv {temp_dir}/TSLA.csv {data_lake}/TSLA_{cur_date}.csv'
)

t5 = PythonOperator(
    task_id='query_data',
    dag=dag,
    python_callable=query,
    op_kwargs={'data_loc': data_lake, 'today_date': cur_date}
)

t0 >> t1
t0 >> t2
t1 >> t3
t2 >> t4
t3 >> t5
t4 >> t5
