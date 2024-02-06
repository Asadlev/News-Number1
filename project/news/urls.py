from django.urls import path
from .views import (
    NewsList, NewsDetail, NewsCreate, NewsUpdate, NewsDelete, AppointmentView
)
from django.views.decorators.cache import cache_page


app_name = 'mails'

urlpatterns = [
    path('', NewsList.as_view(), name='news_list'),
    path('<int:pk>/detail', NewsDetail.as_view(),name='news_detail'),
    path('create/', NewsCreate.as_view(), name='create'),
    path('<int:pk>/update', NewsUpdate.as_view(), name='update'),
    path('<int:pk>/delete', NewsDelete.as_view(), name='delete'),
    path('mails', AppointmentView.as_view(), name='mails'),
]
