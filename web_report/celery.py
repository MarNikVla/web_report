import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_report.settings")

# settings for win10
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app = Celery("web_report")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.broker_url = 'redis://localhost:6379/0'
app.autodiscover_tasks()
