from django.shortcuts import render, HttpResponseRedirect
from webapp.forms import ContactForm, NewsletterForm
from django.contrib import messages


def index_view(request):
    return render(request, 'index.html')


def about_view(request):
    return render(request, 'about.html')


def contact_view(request):
    if request.method == 'POST':
        form_data = ContactForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.add_message(request, messages.SUCCESS, 'save information successfully')
        else:
            messages.add_message(request, messages.ERROR, 'save information not successfully')
    else:
        form_data = ContactForm()
    return render(request, 'contact.html', {'form_data': form_data})


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
