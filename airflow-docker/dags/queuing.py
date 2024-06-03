from airflow import DAG
import pendulum
from airflow.operators.python import PythonOperator
from datetime import datetime

def Hi():
    print("hi")

def howAreYou():
    print("how are you")

def fine():
    print("fine")

with DAG("queue",
    start_date=pendulum.datetime(2024, 5 ,12,tz="Asia/Amman"), 
    schedule='@hourly', 
    catchup=False
    ) as dag:

    hi = PythonOperator(
                task_id="hi",
                python_callable=Hi,
                queue = "saif"
            ) 
    
    howAreYou2 = PythonOperator(
                task_id="howAreYou",
                python_callable=howAreYou,
                queue = "maher"
            ) 
    
    fine2 = PythonOperator(
                task_id="fine",
                python_callable=fine,
                queue = "ahmed"
            ) 
    
    hi >> howAreYou2 >> fine2
