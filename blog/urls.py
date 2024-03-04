from django.urls import path
from blog.views import *


app_name = 'blog_show'

urlpatterns = [
    path('', list_view, name='blog_list'),
    path('<int:pid>', single_view, name='blog_single'),
    path('author/<str:author_username>', list_view, name='author_pubs'),
    path('category/<str:cat_name>', list_view, name='category_blog')
]