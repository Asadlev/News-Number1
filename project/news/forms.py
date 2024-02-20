from django import forms
from .models import News, Appointment
from django.core.exceptions import ValidationError


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            'title',
            'text',
            'category'
        ]

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        if title[0].islower():
            raise ValidationError(
                'Заголовок должен начинаться с заглавной буквы '
            )

        return cleaned_data

    def clean_text(self):
        text = self.cleaned_data['text']
        if len(text) < 20:
            raise ValidationError(
                'Новость не может быть таким коротким'
            )

        return text


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            'client_name',
            'message',
        ]

    def cleaned_name(self):
        cleaned_data = super().clean()
        client_name = cleaned_data.get('client_name')

        if client_name[0].islower():
            raise ValidationError(
                'Имя должно начинаться с Заглавной буквы'
            )

        return cleaned_data

    def cleaned_message(self):
        cleaned_message = super().clean()
        message = cleaned_message.get('message')

        if len(message) < 15:
            raise ValidationError(
                'Сообщение не может быть таким коротким'
            )
