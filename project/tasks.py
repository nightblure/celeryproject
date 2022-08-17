from datetime import datetime, timedelta
from celery import shared_task
from pytz import timezone

from project.celery_ import celery_app
from project.telegram import send_email, send_tg_message


"""
НЕ ПОЛУЧАЕТСЯ ЗАПУСТИТЬ ТАСКИ ЧЕРЕЗ ИНСТАНС СЕЛЕРИ!
"""


""" 
1. ПЕРИОДИЧЕСКИЕ ЗАДАЧИ ПО РАСПИСАНИЮ. вызываются через schedule и celery_beat!
1. запуск celery: celery -A project.celery_.celery_app worker -l info -P solo
2. запуск планировщика celery_beat: celery -A project.celery_.celery_app beat -l info
"""
@shared_task(name='scheduled_task')
# @celery_app.task(name='scheduled_task')
def scheduled_task(*args):
    send_tg_message('hi!')
    # send_email('hello!')


"""
2. ОТЛОЖЕННЫЕ ЗАДАЧИ (ВЫПОЛНЯЮТСЯ 1 РАЗ В ОТЛИЧИЕ ОТ ПЕРИОДИЧЕСКИХ)
чтобы они выполнялись достаточно запустить ТОЛЬКО celery, а затем запустить этот модуль
"""

# эта задача однократно выполнится в заданное время
my_tz = timezone('Asia/Yekaterinburg')
time = my_tz.localize(datetime.now()) + timedelta(minutes=3)
scheduled_task.apply_async(eta=time)
