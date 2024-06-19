from django.shortcuts import render, get_object_or_404
from .models import *


def portfoliosView(request):
    context = {}
    portfolio = PortfolioModel.objects.all()
    promo = PageTitleModel.objects.all()[:1]
    context['portfolio'] = portfolio
    context['promo'] = promo
    return render(request, 'pages/portfolio.html', context)


def individualPortfoliosView(request, slug):
    context = {}
    portfolio = PortfolioModel.objects.get(id=slug)
    blocks = portfolio.blocks.all()
    promo = PageTitleModel.objects.all()[:1]
    context['blocks'] = blocks
    context['promo'] = promo
    return render(request, 'pages/portfolio_individual.html', context)

