from celery import shared_task

from project.telegram import send_email, send_tg_message


@shared_task
def test_task():
    send_email()
    send_tg_message('hi')
