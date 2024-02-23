import os
from celery import Celery
from celery.schedules import crontab
from celery.schedules import solar


os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'project.settings')

app = Celery('project')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# Добавление периодических заданий
app.conf.beat_schedule = {
    'action_every_30_seconds': {
        'task': 'tasks.action',
        'schedule': 5,
        'args': (5, ),
    },
}


'''
Например, чтобы выполнить какую-то задачу 
каждый понедельник в 8 утра, 
необходимо в расписание добавить следующее:
'''
# app.conf.beat_schedule = {
#     'action_every_monday_8am': {
#         'task': 'action',
#         'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
#         'args': ('agrs'),
#     },
# }


'''
    Графики солнечной активности
Если у вас есть задача, 
которая должна выполняться в соответствии с восходом, 
заходом солнца, на рассвете или в сумерках, 
вы можете использовать solar тип расписания:
'''
# solar.conf_beat_schedule = {
#     # Выполняется на закате в Мельбурне
#     'add-at-melbourne-sunset': {
#         'task': 'tasks.add',
#         'schedule': solar('sunset', -37.81753,  144.96715),
#         'аргументы': (16, 16),
#     },
# }



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



