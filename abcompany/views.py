from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from .models import *


def vacancy(request):
    context = {}
    promo = PageTitleModel.objects.all()[:1]
    vacancies = VacancyModel.objects.all()
    context['vacancies'] = vacancies
    context['promo'] = promo
    return render(request, 'pages/vacancy.html', context)


def vacancy_individual(request, slug):
    context = {}
    promo = PageTitleModel.objects.all()[:1]
    vacancy = get_object_or_404(VacancyModel, slug=slug)
    context['vacancy'] = vacancy
    context['promo'] = promo
    return render(request, 'pages/vacancy-individual.html', context)


def partners(request):
    context = {}
    partners = PartnersModel.objects.all()
    promo = PageTitleModel.objects.all()[:1]
    context['partners'] = partners
    context['promo'] = promo
    return render(request, 'pages/partners.html', context)


def partners_individual(request, slug):
    context = {}
    partner = get_object_or_404(PartnersModel, id=slug)
    promo = PageTitleModel.objects.all()[:1]
    context['partner'] = partner
    context['promo'] = promo
    return render(request, 'pages/partners-individual.html', context)


def downloads(request):
    context = {}
    downloads = DownloadsModel.objects.all()
    promo = PageTitleModel.objects.all()[:1]
    context['downloads'] = downloads
    context['promo'] = promo
    return render(request, 'pages/downloads.html', context)


def aboutUs(request):
    context = {}
    promo = PageTitleModel.objects.all()[:1]
    statistics = StatisticsModel.objects.all()[:4]
    missions = MissionModel.objects.all()
    company_missions = CompanyMissionModel.objects.all()[:1]
    team = TeamModel.objects.all()[:6]
    about = AboutUSModel.objects.all()[:1]

    context = {
        'promo': promo,
        'statistics': statistics,
        'missions': missions,
        'company_missions': company_missions,
        'team': team,
        'about': about,
    }

    return render(request, 'pages/about.html', context)


def send_us_cv_view(request):

    context = {}
    promo = PageTitleModel.objects.all()[:1]

    context['promo'] = promo
    form = SendResumeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)

        obj.save()
        form = SendResumeForm()
        return redirect('home')

    context['form'] = form

    return render(request, "contact-us.html", context)

