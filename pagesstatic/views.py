from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Q
from operator import attrgetter
from news.models import *
from portfolio.models import *
from projects.models import *
from abcompany.models import *
from .models import *


def home_screen_view(request):
    context = {}
    query = ''
    if request.GET:
        query = request.GET.get('q', '')
        context['query'] = str(query)

    news = NewsModel.objects.all()
    banner = BannerModel.objects.all()[:1]
    statistics = StatisticsModel.objects.all()[:4]
    portfolio = PortfolioModel.objects.all()[:4]
    projects = ProjectModel.objects.all()
    about = AboutUSModel.objects.all()[:1]
    news_posts = sorted(get_news_queryset(query), key=attrgetter('date_published'), reverse=True)
    context = {
        'news': news_posts,
        'portfolio': portfolio,
        'projects': projects,
        'statistics': statistics,
        'banner': banner,
        'about': about,
    }
    return render(request, 'index.html', context)

class HomeView(TemplateView):
    template_name = 'index.html'


class ContactsView(TemplateView):
    template_name = 'contacts.html'


class NewsView(TemplateView):
    template_name = 'news.html'


class PortfolioView(TemplateView):
    template_name = 'portfolio.html'


class ProjectsView(TemplateView):
    template_name = 'projects.html'


def about_page(request):
    context = {}
    return render(request, 'about.html', context)


def just_page(request):
    context = {}
    return render(request, 'about.html', context)


def get_news_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        posts = NewsModel.objects.filter(
            Q(name__icontains=q) |
            Q(text__icontains=q)
        ).distinct()

        for post in posts:
            queryset.append(post)

    return list(set(queryset))