from datetime import datetime, timedelta
from time import sleep
from celery import shared_task
from celery.result import AsyncResult
from pytz import timezone
from project.telegram import send_email, send_tg_message
from celery import Celery

# обязательно нужно импортировать файл с тасками в include, либо обычным import
celery_app = Celery('tasks', include=['project.tasks'])
celery_app.config_from_object('project.settings', namespace='CELERY')
celery_app.autodiscover_tasks()

# region ПЕРИОДИЧЕСКИЕ ЗАДАЧИ ПО РАСПИСАНИЮ

""" 
1. ПЕРИОДИЧЕСКИЕ ЗАДАЧИ ПО РАСПИСАНИЮ. вызываются через schedule и celery_beat!
1. запуск celery: celery -A project.tasks.celery_app worker -l info -P solo
2. запуск планировщика celery_beat: celery -A project.tasks.celery_app beat -l info
3. celery сделает все сам, нужно лишь ждать сообщений в телеге каждые 2 секунды
"""


# @shared_task(name='scheduled_task')
@celery_app.task(name='scheduled_task')
def scheduled_task(*args):
    pass
    send_tg_message('hi!')
    # send_email('hello!')


# endregion

# region ОТЛОЖЕННЫЕ ЗАДАЧИ

"""
2. ОТЛОЖЕННЫЕ ЗАДАЧИ (ВЫПОЛНЯЮТСЯ 1 РАЗ В ОТЛИЧИЕ ОТ ПЕРИОДИЧЕСКИХ)
чтобы они выполнялись достаточно запустить ТОЛЬКО celery, а затем запустить этот модуль
"""

# эта задача однократно выполнится в заданное время
my_tz = timezone('Asia/Yekaterinburg')
time = my_tz.localize(datetime.now()) + timedelta(minutes=3)
# scheduled_task.apply_async(eta=time)

# endregion

# region ПОЛУЧЕНИЕ РЕЗУЛЬТАТОВ ЗАДАЧ

"""
ЗАДАЧА: есть три таска, которые спят разное время и возвращают одно значение
задача в том, чтобы запустить их, дождаться окончания выполнения и вывести результаты

ГАЙД: запустить celery (без планировщика) и в python console вставить следующий код:

from project.tasks import *
tasks = [task1, task2, task3]
tasks = {task: task.apply_async() for task in tasks}

finished_tasks_count = 0

while finished_tasks_count < 3:

    for task in tasks:
   
        result = tasks[task]

        if result.state == 'SUCCESS':
            finished_tasks_count += 1

# вывод результатов выполнения тасков
[print(tasks[task].get()) for task in tasks.keys()]
 
"""


@celery_app.task(name='task1', ignore_result=False)
def task1():
    sleep(15)
    print('task1 finish')
    return 'task1 finish'


@celery_app.task(name='task2', ignore_result=False)
def task2():
    sleep(12)
    print('task2 finish')
    return 'task2 finish'


@celery_app.task(name='task3', ignore_result=False)
def task3():
    sleep(8)
    print('task3 finish')
    return 'task3 finish'

# endregion
