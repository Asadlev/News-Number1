from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Appointment
from django.core.mail import mail_managers
from django.db.models.signals import post_delete


@receiver(post_save, sender=Appointment)
# D9.4. Отправка электронных писем по событию, знакомство с сигналами
def notify_managers_appointment(sender, instance, created, **kwargs):
    # в зависимости от того, есть ли такой объект уже в базе данных или нет, тема письма будет разная
    if created:
        subject = f'{instance.client_name} {instance.date.strftime("%y-%m-%d")}'
    else:
        subject = f'Appointment changed for {instance.client_name} {instance.date.strftime("%y-%m-%d")}'

    mail_managers(
        subject=subject,
        message=instance.message,
    )
    print(f'{instance.client_name} {instance.date.strftime("%y-%m-%d")}')

# Вместо того чтобы коннектить - post_save.connect(notify_managers_appointment, sender=Appointment). Можно еще сделать дело с декоратором - @receiver(post_save, sender=Appointment)


# Это функция Чтобы сообщалось об удалений
@receiver(post_delete, sender=Appointment)
def post_delete_appointment(sender, instance, **kwargs):
    if kwargs:
        subject = f'Appointment in the delete! {instance.client_name} {instance.date.strftime("%y-%m-%d")}'
    else:
        subject = f'{instance.client_name} {instance.date.strftime("%y-%m-%d")}'

    mail_managers(
        subject=subject,
        message=instance.message,
    )
    print(f'{instance.client_name} {instance.date.strftime("%y-%m-%d")}')

