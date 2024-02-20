from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import BaseRegisterForm
from django.contrib.auth.models import User


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/sign/login/'


