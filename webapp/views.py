from django.shortcuts import render, redirect
from webapp.forms import ContactForm  #,NewsletterForm
from django.contrib import messages


def index_view(request):
    return render(request, 'index.html')


def about_view(request):
    return render(request, 'about.html')


def contact_view(request):
    if request.method == 'POST':
        form_data = ContactForm(request.POST)
        if form_data.is_valid():
            contact = form_data.save()
            contact.save()
            messages.add_message(request, messages.SUCCESS, 'save information successfully')
        else:
            messages.add_message(request, messages.ERROR, 'save information not successfully')
    form_data = ContactForm()
    return render(request, 'contact.html', {'form_data': form_data})

