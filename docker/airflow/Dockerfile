FROM puckel/docker-airflow:1.10.9

USER root
RUN apt-get update && apt-get install -y procps

RUN apt-get install -y wget
RUN apt-get install -y gnupg2
RUN apt-get install -y lsb-release
RUN echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN apt-get update
RUN apt-get install -y postgresql postgresql-client

RUN apt-get install -y openssh-client
RUN curl -O https://cli-dl.scalingo.io/install && bash install
RUN apt-get install lsof
RUN apt-get update && apt-get install -y git

RUN mkdir -m 766 /code
WORKDIR /code
RUN git clone https://github.com/betagouv/pass-culture-data-analytics.git
RUN pwd && cd pass-culture-data-analytics && git checkout PC-3921-add-metabase-cli && pip install -e .
#ENV AIRFLOW_HOME=/usr/local/airflow
#COPY ./airflow.cfg /usr/local/airflow/airflow.cfg
