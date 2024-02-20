from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import BaseRegisterView
from django.views.decorators.cache import cache_page

urlpatterns = [
    # cache - path('login/', cache_page(60*10)(LoginView.as_view(template_name='sign/login.html')), name='login'),
    path('login/', LoginView.as_view(template_name = 'sign/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'sign/logout.html'), name='logout'),
    path('signup/', BaseRegisterView.as_view(template_name='sign/signup.html'), name='signup'),

]

