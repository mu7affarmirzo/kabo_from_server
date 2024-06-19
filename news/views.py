from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from operator import attrgetter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import *
from django.http import HttpResponse
BLOG_POSTS_PER_PAGE = 3

# Create your views here.


def news_view(request):
    context = {}
    query = ''
    if request.GET:
        query = request.GET.get('q', '')
        context['query'] = str(query)

    news_posts = sorted(get_news_queryset(query), key=attrgetter('date_published'), reverse=True)
    context['news_posts'] = news_posts

    page = request.GET.get('page', 1)
    news_posts_paginator = Paginator(news_posts, BLOG_POSTS_PER_PAGE)

    try:
        news_posts = news_posts_paginator.page(page)
    except PageNotAnInteger:
        news_posts = news_posts_paginator.page(BLOG_POSTS_PER_PAGE)
    except EmptyPage:
        news_posts = news_posts_paginator.page(news_posts_paginator.num_pages)

    context['news_posts'] = news_posts

    promo = PageTitleModel.objects.all()[:1]
    context['promo'] = promo
    return render(request, 'pages/news.html', context)


def detail_news_view(request, slug):
    context = {}

    news_post = get_object_or_404(NewsModel, slug=slug)
    promo = PageTitleModel.objects.all()[:1]
    context['news_post'] = news_post
    context['promo'] = promo

    return render(request, 'pages/news_item.html', context)


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
