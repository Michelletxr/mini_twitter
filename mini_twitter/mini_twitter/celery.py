import os

from celery import Celery, shared_task

from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mini_twitter.settings")

app = Celery("mini_twitter")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.broker_url = settings.REDIS_URL
app.autodiscover_tasks()


