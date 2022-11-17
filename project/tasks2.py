from datetime import datetime, timedelta
from time import sleep
from pytz import timezone
from project import celery_app
from project.telegram import send_tg_message
from tasks import tg_task3


# эта задача однократно выполнится в заданное время
my_tz = timezone('Asia/Yekaterinburg')
time = my_tz.localize(datetime.now()) + timedelta(minutes=1)
tg_task3.apply_async(eta=time, queue='queue2')
