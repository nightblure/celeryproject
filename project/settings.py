from datetime import timedelta
from project import celery_app
from celery.schedules import crontab

# порты смотреть в докере!
REDIS_PORT = 6379
RABBITMQ_PORT = 5672

REDIS_BROKER_URL = f'redis://localhost:{REDIS_PORT}'
RABBITMQ_BROKER_URL = f'amqp://guest:guest@localhost:{RABBITMQ_PORT}'  # 'amqp://localhost'

CELERY_BROKER_URL = REDIS_BROKER_URL

# в качестве бэкенда используем redis
CELERY_RESULT_BACKEND = 'redis://'  # f'redis://localhost:{REDIS_PORT}'

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

# расписание для выполнения периодических (запланированных задач)
celery_app.conf.beat_schedule = {
    # имя
    'test_delayed_task_name': {
        # путь к задаче. если не работает, нужно оставить только название таска
        'task': 'scheduled_task',
        # кулдаун выполнения (минимальный - 1 минута)
        # 'schedule': crontab(minute=1)
        # по секундам можно выполнять с помощью timedelta
        'schedule': timedelta(seconds=2)
    }
}