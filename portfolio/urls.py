from .views import *
from django.urls import path

app_name = 'portfolio'

urlpatterns = [
    path('portfolio/', portfoliosView, name='portfolio'),
    path('portfolio/<slug>', individualPortfoliosView, name='portfolio-individual'),
]
