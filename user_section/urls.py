from django.urls import path
from user_section.views import *


app_name = 'user_auth'

urlpatterns = [

    path('signup', signup_view, name='signup_page'),

]