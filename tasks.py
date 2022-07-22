from celery import shared_task
import datetime

@shared_task
def test_task():

    with open('tasks_log.txt', 'a') as file:
        file.write(f"task info.. | {datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')}\n")