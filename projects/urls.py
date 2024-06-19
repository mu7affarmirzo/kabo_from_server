from .views import *
from django.urls import path

app_name = 'projects'

urlpatterns = [
    path('projects/', projectsView, name='projects'),
    path('projects/<slug>', individualProjectsView, name='projects-individual'),
]
