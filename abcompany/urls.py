from .views import *
from django.urls import path

app_name = 'abcompany'

urlpatterns = [
    path('about-us/', aboutUs, name='about-us'),
    path('vacancy/', vacancy, name='vacancy'),
    path('vacancy/<slug>', vacancy_individual, name='vacancy-individual'),
    path('partners/', partners, name='partners'),
    path('partners/<slug>', partners_individual, name='partners-individual'),
    path('cv-send', send_us_cv_view, name='send-cv'),
    path('downloads/', downloads, name='downloads'),
]
