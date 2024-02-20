import os
from celery import Celery
from celery.schedules import crontab
from celery.schedules import solar


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


# CELERY_BEAT_SCHEDULE = {
#     'send-newsletter': {
#         'task': 'news.tasks.send_notification_email',
#         'schedule': crontab(day_of_week=1, hour=8, minute=0),
#     },
# }
#
#
# CELERY_BEAT_SCHEDULE = {
#     'send-newsletter': {
#         'task': 'news.tasks.send_newsletter',
#         'schedule': crontab(day_of_week=1, hour=8, minute=0),
#     },
# }



