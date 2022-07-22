from celery import shared_task
import datetime

from project.telegram import send_message, send_email


@shared_task
def test_task():
    send_email()
    #send_message('555235552326282:AAHDk4hNElVZI4QAox5552326282:AAHDk4hNElVZI4QAoxa9RlZICvZo_QwWZwwa9RlZICvZo_QwW5552326282:AAHDk4hNElVZI45552326282:AAHDk4hNElVZI4QAoxa9RlZICvZo_QwWZwwQAoxa9RlZICvZo_QwWZwwZww26282:AAHDk4hNElVZI4QAoxa9RlZICvZo_QwWZww')
    # with open('tasks_log.txt', 'a') as file:
    #     file.write(f"task info.. | {datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')}\n")