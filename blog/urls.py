from django.urls import path
from blog.views import *


app_name = 'blog_show'

urlpatterns = [
    path('', home_view, name='home_blog'),

]