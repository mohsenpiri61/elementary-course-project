from django.urls import path
from blog.views import *


app_name = 'blog_show'

urlpatterns = [
    path('', list_view, name='blog_list'),
    path('<int:pid>', single_view, name='blog_single'),
]