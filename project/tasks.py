from datetime import datetime, timedelta
from time import sleep

from celery import shared_task
from celery.result import AsyncResult
from kombu import Exchange, Queue
from pytz import timezone
from project.telegram import send_email, send_tg_message
from celery import Celery

# region celery instance
# обязательно нужно импортировать файл с тасками в include, либо обычным import
celery_app = Celery('tasks', include=['project.tasks'])

celery_app.conf.task_queues = (
    Queue('queue1', routing_key='default'),
    Queue('queue2', routing_key='media.video'),
)

celery_app.config_from_object('project.settings', namespace='CELERY')
celery_app.autodiscover_tasks()
# endregion

# region ПЕРИОДИЧЕСКИЕ ЗАДАЧИ ПО РАСПИСАНИЮ

""" 
1. ПЕРИОДИЧЕСКИЕ ЗАДАЧИ ПО РАСПИСАНИЮ. вызываются через schedule и celery_beat!
    1. запуск celery: celery -A project.tasks.celery_app worker -l info -P solo
    2. запуск планировщика celery_beat: celery -A project.tasks.celery_app beat -l info
    3. мониторинг в flower: celery -A project.tasks.celery_app flower
"""


# @shared_task(name='scheduled_task')
@celery_app.task(name='tg_task1')
def tg_task1(*args):
    sleep(4.5)
    send_tg_message('task 1!')


@celery_app.task(name='tg_task2')
def tg_task2(*args):
    sleep(3)
    send_tg_message('task 2!')


@celery_app.task(name='tg_task3')
def tg_task3(*args):
    sleep(3)
    send_tg_message('task 3!')


@celery_app.task(name='mail_task')
def mail_task(*args):
    send_email('hello!')

# endregion

# region ОТЛОЖЕННЫЕ ЗАДАЧИ

"""
2. ОТЛОЖЕННЫЕ ЗАДАЧИ (ВЫПОЛНЯЮТСЯ 1 РАЗ В ОТЛИЧИЕ ОТ ПЕРИОДИЧЕСКИХ)
чтобы они выполнялись достаточно запустить ТОЛЬКО celery, а затем запустить этот модуль
"""

# endregion

# region ПОЛУЧЕНИЕ РЕЗУЛЬТАТОВ ЗАДАЧ

"""
ЗАДАЧА: есть три таска, которые спят разное время и возвращают одно значение
задача в том, чтобы запустить их, дождаться окончания выполнения и вывести результаты

ГАЙД: запустить celery без планировщика (celery -A project.tasks.celery_app worker -l info -P solo) 
и в python console выполнить код:

from project.tasks import *
tasks = [task1, task2, task3]    
tasks = {task: task.apply_async() for task in tasks}

finished_tasks_count = 0

while finished_tasks_count < len(tasks):
    
    for task in tasks: 
        if tasks[task].state == 'SUCCESS':
            finished_tasks_count += 1

# вывод результатов выполнения тасков
[print(tasks[task].get()) for task in tasks.keys()]
 
"""


@celery_app.task(name='task1', ignore_result=False)
def task1():
    sleep(10)
    print('task1 finish')
    return 'task1 finish'


@celery_app.task(name='task2', ignore_result=False)
def task2():
    sleep(8)
    print('task2 finish')
    return 'task2 finish'


@celery_app.task(name='task3', ignore_result=False)
def task3():
    sleep(5)
    print('task3 finish')
    return 'task3 finish'

# endregion
