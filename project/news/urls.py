from django.urls import path
from .views import (
    NewsList, NewsDetail, NewsCreate, NewsUpdate, NewsDelete, SuccessView,
)
from .mails import AppointmentView
from django.views.decorators.cache import cache_page
from . import views


app_name = 'mails'

urlpatterns = [
    path('', NewsList.as_view(), name='news_list'),
    path('<int:pk>/detail', NewsDetail.as_view(),name='news_detail'),
    path('create/', NewsCreate.as_view(), name='create'),
    path('<int:pk>/news_update', NewsUpdate.as_view(), name='news_update'),
    path('<int:pk>/news_delete', NewsDelete.as_view(), name='news_delete'),
    path('mails', AppointmentView.as_view(), name='mails'),
    path('success', SuccessView.as_view(), name='success'),
]
