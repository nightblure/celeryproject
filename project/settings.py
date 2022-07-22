from datetime import timedelta
from celery.schedules import crontab


# порты смотреть в докере!

REDIS_PORT = 6379
RABBITMQ_PORT = 5672

REDIS_BROKER_URL = f'redis://localhost:{REDIS_PORT}'
RABBITMQ_BROKER_URL = f'amqp://guest:guest@localhost:{RABBITMQ_PORT}' # 'amqp://localhost'

CELERY_BROKER_URL = RABBITMQ_BROKER_URL

# в качестве бэкенда используем redis
CELERY_RESULT_BACKEND = 'redis://' # f'redis://localhost:{REDIS_PORT}'

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

CELERY_BEAT_SCHEDULE = {
    # имя
    'test_delayed_task_name': {
        # путь к задаче
        'task': 'tasks.test_task',
        # кулдаун выполнения (минимальный - 1 минута)
        #'schedule': crontab(minute=1)
        # по секундам можно выполнять с помощью timedelta
        'schedule': timedelta(seconds=3)
    }
}