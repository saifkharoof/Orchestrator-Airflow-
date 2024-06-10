FROM apache/airflow:2.9.0
USER root
RUN apt update
RUN apt install -y chromium
USER airflow
RUN pip install selenium
RUN pip install webdriver_manager
