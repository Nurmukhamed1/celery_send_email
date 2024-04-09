import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_docker.settings')

app = Celery('celery_docker')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-spam-every-1-minute': {
        'task': 'send_email.tasks.send_spam_beats',
        'schedule': crontab(minute='*/1'),
    },
}
