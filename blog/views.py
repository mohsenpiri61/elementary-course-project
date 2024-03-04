from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Comment
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

"""
from blog.forms import CommentForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
"""


def list_view(request, **kwargs):
    filter_post = Post.objects.filter(published_date__lt=timezone.now(), status=1)
    if kwargs.get('cat_name') != None:
        filter_post = filter_post.filter(category_list__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        filter_post = filter_post(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        filter_post = filter_post.filter(tags__name__in=[kwargs['tag_name']])

    page_init = Paginator(filter_post, 3)
    page_number = request.GET.get('page')

    try:
        filter_post = page_init.get_page(page_number)
    except PageNotAnInteger:
        filter_post = page_init.page(1)
    except EmptyPage:
        filter_post = page_init.page(page_init.num_pages)
    context = {'filter_post': filter_post}
    return render(request, 'blog_items/blog-list.html', context)


def single_view(request):
    return render(request, 'blog_items/blog-single.html')
