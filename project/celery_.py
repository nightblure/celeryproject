import celery

# обязательно нужно импортировать файл с тасками в include, либо обычным import
celery_app = celery.Celery('tasks', include=['project.tasks'])
celery_app.config_from_object('project.settings', namespace='CELERY')
celery_app.autodiscover_tasks()
