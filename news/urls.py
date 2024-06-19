from .views import *
from django.urls import path

app_name = 'news'

urlpatterns = [
    path('', news_view, name='news'),
    path('<slug>', detail_news_view, name='news-individual'),
]
