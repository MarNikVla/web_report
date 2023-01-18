import time

from celery import shared_task
from django.core.files.storage import default_storage


@shared_task
def del_file_task(file_path='fsdfs'):
    print('start')
    default_storage.delete(file_path)
    print('dfsdf')
    return 'Done'