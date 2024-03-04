from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Comment
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.forms import CommentForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def list_view(request, **kwargs):
    filter_post = Post.objects.filter(published_date__lt=timezone.now(), status=1)
    if kwargs.get('cat_name') != None:
        filter_post = filter_post.filter(category_list__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        filter_post = filter_post.filter(author__username=kwargs['author_username'])
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


def single_view(request, pid):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            messages.add_message(request, messages.SUCCESS, 'Your comment submitted successfully.')
        else:
            messages.add_message(request, messages.ERROR, "Your comment didn't submitted .")
    else:
        comment_form = CommentForm()
    # showing each post Section
    post_obj = get_object_or_404(Post, id=pid, status=1, published_date__lt=timezone.now())
    post_obj.counted_views = post_obj.counted_views + 1
    post_obj.save()

    if not post_obj.login_needed or request.user.is_authenticated:

        comments = Comment.objects.filter(intended_post=post_obj.id, approved=True)
        # Next and Previous Section
        filter_post = Post.objects.filter(published_date__lt=timezone.now(), status=1)
        post_ids = [post.id for post in filter_post]
        pid_index = post_ids.index(pid)
        if pid_index == 0:
            next_id = post_ids[pid_index + 1]
            next_post = Post.objects.get(id=next_id)
            prev_post = None
        elif pid_index == post_ids.index(post_ids[-1]):
            prev_id = post_ids[pid_index - 1]
            prev_post = Post.objects.get(id=prev_id)
            next_post = None
        else:
            next_id = post_ids[pid_index + 1]
            next_post = Post.objects.get(id=next_id)
            prev_id = post_ids[pid_index - 1]
            prev_post = Post.objects.get(id=prev_id)

        context = {'post_obj': post_obj, 'next_post': next_post, 'prev_post': prev_post, 'comments': comments}
        return render(request, 'blog_items/blog-single.html', context)

    else:
        return HttpResponseRedirect(reverse('user_auth:login_page'))


def search_view(request):
    filter_post = Post.objects.filter(published_date__lt=timezone.now(), status=1)
    if request.method == 'GET':
        req = request.GET.get('s')
        if req:
            filter_post = filter_post.filter(content__contains=req)
    context = {'filter_post': filter_post}
    return render(request, 'blog_items/blog-home.html', context)
