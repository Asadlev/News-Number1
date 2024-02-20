from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.cache import cache


class News(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='news',
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('mails:news_detail', args=[str(self.id)])

    # def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
    #     return f'/news_list/{self.id}'
    #
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)  # сначала вызываем метод родителя, чтобы объект сохранился
    #     cache.delete(f'-news_detail-{self.pk}')  # затем удаляем его из кэша, чтобы сбросить его


class Category(models.Model):
    name = models.CharField(max_length=255)
    subscribers = models.ManyToManyField(User, related_name='subscribed_categories')


class Appointment(models.Model):
    date = models.DateTimeField(
        default=datetime.utcnow,
    )
    client_name = models.CharField(
        max_length=49,
    )
    message = models.TextField()

