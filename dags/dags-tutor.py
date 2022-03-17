from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

# default args which can be overridden later on
args = {
    'owner' : 'Admin', 
    'start_date' : datetime(2022, 3, 16),
    #'retries' : 1,
    #'retry_delay': timedelta(minutes=10),
    'provide_context':True
}

# define simple test function
def print_world() :
    print('Python printing...')

# define DAG
with DAG('airflow_dags_tutorial',
        description='Simple Hello dag',
        schedule_interval='*/1 * * * *', # https://crontab.guru/#0_*_*_*_*
        catchup=False,
        default_args=args
        ) as dag :
    task1 = BashOperator(
        task_id='task_1',
        bash_command='echo "Hello task 1"'
    )
    task2 = BashOperator(
        task_id='task_2',
        bash_command='echo "Hello task 2"'
    )
    task3 = BashOperator(
        task_id='task_3',
        bash_command='echo "Hello task 3"'
    )
    task4 = PythonOperator(
        task_id='task4',
        python_callable=print_world
    )

    task1 >> task2
    task1 >> task3
    task2 >> task4

# END 

