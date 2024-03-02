#from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
#from webapp.models import Contact
#from webapp.forms import NameForm, ContactForm, NewsletterForm
#from django.contrib import messages


def index_view(request):
    return render(request, 'index.html')


def about_view(request):
    return render(request, 'about.html')


def contact_view(request):
    return render(request, 'contact.html')
