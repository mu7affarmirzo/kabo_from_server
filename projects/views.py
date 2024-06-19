from django.shortcuts import render, get_object_or_404
from .models import *


def projectsView(request):
    context = {}
    projects = ProjectModel.objects.all()
    promo = PageTitleModel.objects.all()
    context['projects'] = projects
    context['promo'] = promo
    return render(request, 'pages/projects.html', context)


def individualProjectsView(request, slug):
    context = {}
    project = ProjectModel.objects.get(id=slug)
    promo = PageTitleModel.objects.all()
    blocks = project.blocks.all()
    context['blocks'] = blocks
    context['promo'] = promo
    return render(request, 'pages/projects_individual.html', context)

