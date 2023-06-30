import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "back_groud_tasks.settings")

celery = Celery("back_groud_tasks")
celery.config_from_object("django.conf:settings", namespace="CELERY")
celery.autodiscover_tasks()