from django import forms
from webapp.models import Contact, Newsletter


# from captcha.fields import ReCaptchaField


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'
