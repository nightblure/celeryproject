import requests
import smtplib, ssl

BOT_TOKEN = '5552326282:AAHDk4hNElVZI4QAoxa9RlZICvZo_QwWZww'
BOT_NAME = 'inzera_bot'
GROUP_ID = '-685273008'
TELEGRAM_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'


def send_message(text, reciever_id=GROUP_ID):
    requests.post(TELEGRAM_URL, json={
        'chat_id': reciever_id,
        'text': text
    })


def send_email():

    message = f'Я родился на блоке мама в 1991 г. \
        Но развал Советского Союза заставил мою семью уехать в Украину \
        из этого города, поскольку влияние развала сильно отразилось на уровне жизни \n \
        Стало хорошо, мы стали жить в полном благополучии, позже у меня родились две сестры \
        Но когда я закончил школу, по всей территории начались беспокойства и боевые стычки \n \
        Со временем обстановка все ухудшалась, т.к. военные действия стали проходить все ближе \
        к населенным пунктам, стали призывать всех обороняться \n Я ушел воевать \
        3 года назад уехал оттуда в Россию со всей семьей, помирать там не хотелось бы, удалось вырваться \n \
        Теперь живем в Перми, но хотелось бы вернуться обратно в Краснодон, \
        о чем я часто пишу своему брату в письмах \
        (брату Dyrov Ramzanka, который тебе пересылал мое сообщение о Краснодоне) \n \
        А рассказывать про то, как я попал в петер, думаю излишне'.encode('utf-8')

    sender = 'vanobel159@gmail.com'
    password = 'cawzihgzhuyzromu'
    reciever = 'sapas1303@gmail.com'
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender, password)
        server.sendmail(
            sender,
            reciever,
            message,
        )
