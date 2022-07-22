import os
import celery

from tasks import test_task

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
celery_app = celery.Celery('project')
celery_app.config_from_object('project.settings', namespace='CELERY')
celery_app.autodiscover_tasks()

