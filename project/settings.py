from datetime import timedelta
from .tasks import celery_app
from celery.schedules import crontab

# порты смотреть в докере!
REDIS_PORT = 6379
RABBITMQ_PORT = 5672

REDIS_BROKER_URL = f'redis://localhost:{REDIS_PORT}'
RABBITMQ_BROKER_URL = f'amqp://guest:guest@localhost:{RABBITMQ_PORT}'  # 'amqp://localhost'

CELERY_BROKER_URL = REDIS_BROKER_URL

# в качестве бэкенда (бэкенд хранит результаты тасков) используем redis
CELERY_RESULT_BACKEND = REDIS_BROKER_URL

# CELERY_TASK_ROUTES = {
#     # можно указать все задачи: project.tasks.*
#     'project.tasks.tg_task1': {'queue': 'queue1'},
#     'project.tasks.tg_task2': {'queue': 'queue2'},
# }

# настройка redis
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'redis://localhost:{REDIS_PORT}',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient'
        }
    }
}

# CELERY_TASK_TRACK_STARTED = True

# расписание для выполнения периодических (запланированных задач)
celery_app.conf.beat_schedule = {
    # имя
    'tg1': {
        # путь к задаче. если не работает, нужно оставить только название таска
        'task': 'tg_task1',
        # кулдаун выполнения (минимальный - 1 минута)
        # 'schedule': crontab(minute=1)
        # по секундам можно выполнять с помощью timedelta
        'schedule': timedelta(seconds=2),
        'options': {'queue': 'queue1'}
    },

    'tg2': {
        'task': 'tg_task2',
        'schedule': timedelta(seconds=2),
        'options': {'queue': 'queue2'}
    },

    # 'email_task': {
    #     'task': 'mail_task',
    #     'schedule': timedelta(seconds=2)
    # }
}
