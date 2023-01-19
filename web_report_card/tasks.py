from celery import shared_task
from django.core.files.storage import default_storage


@shared_task
def del_file_task(file_path):
    print('start')
    default_storage.delete(file_path)
    print('finish')
    return 'Done'