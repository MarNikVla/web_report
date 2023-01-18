import os
import sys

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_report.settings")

app = Celery("web_report")
app.config_from_object("django.conf:settings", namespace="CELERY")

if sys.platform == 'win32':
    os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app.autodiscover_tasks()
