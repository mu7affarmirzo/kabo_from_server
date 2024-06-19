from .views import *
from django.urls import path

app_name = 'contacts'

urlpatterns = [
    path('', contact_us_view, name='contacts'),
]
