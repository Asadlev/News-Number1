from celery import shared_task
from django.core.mail import mail_managers
from django.contrib.auth.models import User
from .models import News, Appointment


# @shared_task
# def send_notification_email(news_id):
#     news = News.objects.get(pk=news_id)
#     subscribers = User.objects.filter(subscribe=True)
#
#     for subscriber in subscribers:
#         send_mail(
#             'New News Notification',
#             f'Hello {subscriber.username},\n\nA new news has been posted: {news.title}',
#             'imaralievasadbek@yandex.ru',
#             ['imaraliev.kg2005@gmail.com'],
#             fail_silently=False,
#         )
#
#
# @shared_task
# def send_newsletter():
#     latest_news = News.objects.order_by('-text')[:5]
#     subscribers = User.objects.filter(subscribe=True)
#
#     for subscriber in subscribers:
#         send_mail(
#             'Weekly Newsletter',
#             f'Hello {subscriber.username},\n\nHere are the latest news:\n\n{latest_news}',
#             'imaralievasadbek@yandex.ru',
#             ['imaraliev.kg2005@gmail.com'],
#             fail_silently=False,
#         )


# task - scheduler
def send_mails(**kwargs):
    print('hello from task! send_mails')
