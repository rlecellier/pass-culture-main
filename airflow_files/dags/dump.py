from datetime import timedelta

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to operate!
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}
dag = DAG(
    'dump_restore',
    default_args=default_args,
    description='Dump production database and restore it to pc-data-analytics-datasource',
    schedule_interval=timedelta(days=1),
    catchup=False,
)

# t1, t2 and t3 are examples of tasks created by instantiating operators


t1 = BashOperator(
    task_id='dump',

    # This fails with 'Jinja template not found' error
    # bash_command="/home/batcher/test.sh",

    # This works (has a space after)
    bash_command="/config/scalingo/partial_backup/partial_backup.sh -a pass-culture-api-dev ",
    dag=dag)


t2 = BashOperator(
    task_id='clear',

    # This fails with 'Jinja template not found' error
    # bash_command="/home/batcher/test.sh",

    # This works (has a space after)
    bash_command="/config/scalingo/clean_database.sh pc-data-analytics show_app_name_for_restore ",
    dag=dag)


t3 = BashOperator(
    task_id='restore',

    # This fails with 'Jinja template not found' error
    # bash_command="/home/batcher/test.sh",

    # This works (has a space after)
    bash_command="/config/scalingo/restore_database.sh pc-data-sandbox ",
    dag=dag)


t4 = BashOperator(
    task_id='anonymize',

    # This fails with 'Jinja template not found' error
    # bash_command="/home/batcher/test.sh",

    # This works (has a space after)
    bash_command="/config/scalingo/anonymize_db_env.sh pc-data-sandbox ",
    dag=dag)


t1 >> t2 >> t3 >> t4