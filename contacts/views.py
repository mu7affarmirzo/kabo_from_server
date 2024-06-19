from django.shortcuts import render, redirect
from contacts.models import *
from contacts.forms import *

# Create your views here.
def contact_us_view(request):

    context = {}

    form = ContactUsForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)

        obj.save()
        form = ContactUsForm()
        return redirect('home')

    context['form'] = form

    return render(request, "contact-us.html", context)
