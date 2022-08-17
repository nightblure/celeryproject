import smtplib
import ssl

import requests

BOT_TOKEN = '5552326282:AAHDk4hNElVZI4QAoxa9RlZICvZo_QwWZww'
BOT_NAME = 'inzera_bot'
GROUP_ID = '-685273008'
TELEGRAM_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'


def send_tg_message(text, reciever_id=GROUP_ID):
    requests.post(TELEGRAM_URL, json={
        'chat_id': reciever_id,
        'text': text
    })


def send_email(text):

    message = text
    message = message.encode('utf-8')

    sender = 'vanobel159@gmail.com'
    password = 'cawzihgzhuyzromu'
    reciever = sender # 'sapas1303@gmail.com'
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender, password)
        server.sendmail(
            sender,
            reciever,
            message,
        )
