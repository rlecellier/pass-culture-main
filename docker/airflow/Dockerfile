FROM puckel/docker-airflow:1.10.9

USER root
RUN apt-get update && apt-get install -y procps
RUN apt-get install -y postgresql postgresql-client
RUN apt-get install -y openssh-client
RUN curl -O https://cli-dl.scalingo.io/install && bash install


USER airflow
#ENV AIRFLOW_HOME=/usr/local/airflow
#COPY ./airflow.cfg /usr/local/airflow/airflow.cfg
