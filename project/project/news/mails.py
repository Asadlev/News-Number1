from django.core.mail import mail_managers
from django.shortcuts import redirect, render
from django.views.generic import View
from .models import Appointment
from datetime import datetime


class AppointmentView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mails.html')

    def post(self, request, *args, **kwargs):
        appointment = Appointment(
            date=datetime.strptime(request.POST['date'], '%Y-%m-%d'),
            client_name=request.POST['client_name'],
            message=request.POST['message'],
        )
        appointment.save()

        '''
            Отправка html
        '''
        # Получаем наш html
        # html_content = render_to_string(
        #     'mails_created.html',
        #     {
        #         'mails': appointment,
        #     }
        # )
        # # в конструкторе уже знакомые нам параметры, да? Называются правда немного по-другому, но суть та же.
        # msg = EmailMultiAlternatives(
        #     subject=f'{appointment.client_name} {appointment.date.strftime("%Y-%M-%d")}',
        #     body=appointment.message,  # это то же, что и recipients_list
        #     from_email='imaralievasadbek@yandex.ru',
        #     to=['imaraliev.kg2005@gmail.com'],
        # )
        # msg.attach_alternative(html_content, 'text/html')  # Добавляем html
        # msg.send()  # Отправить

        '''
            Отправка Пользователю(по отдельности)
        '''
        # send_mail(
        #     subject=f'{appointment.client_name}: {appointment.date.strftime("%Y-%m-%d")}',
        #     message=appointment.message,
        #     from_email='imaralievasadbek@yandex.ru',
        #     recipient_list=['imaraliev.kg2005@gmail.com']
        # )

        '''
            Отправка админам
        '''
        # отправляем письмо всем админам по аналогии с send_mail, только здесь получателя указывать не надо
        # mail_admins(
        #     subject=f'{appointment.client_name} {appointment.date.strftime("%Y-%m-%d")}',
        #     message=appointment.message,
        # )

        '''
            Отправка менеджерам
        '''
        mail_managers(
            subject=f'{appointment.client_name} {appointment.date.strftime("%Y-%m-%d")}',
            message=appointment.message,

        )

        return redirect('mails:success')