from django import template
from blog.models import Post, Category, Comment
from django.utils import timezone

register = template.Library()


@register.simple_tag(name='posts')
def show_post():
    posts_obj = Post.objects.filter(status=1)
    return posts_obj


@register.simple_tag(name='comments_count')
def show_comments_count(pid):
    return Comment.objects.filter(intended_post=pid, approved=True).count()


@register.filter
def snippet(value, count):
    return value[:count]


@register.inclusion_tag('popular-post-view.html')
def show_latest_posts():
    post_obj = Post.objects.filter(status=1).order_by('-published_date')[:3]
    return {'post_obj': post_obj}


@register.inclusion_tag('blog_items/popular-posts.html')
def most_visited_posts(arg=3):
    post_obj = Post.objects.filter(published_date__lt=timezone.now(), status=1).order_by('-counted_views')[:arg]
    return {'post_obj': post_obj}


@register.inclusion_tag('blog_items/blog-category.html')
def cat_of_posts():
    post_obj = Post.objects.filter(published_date__lt=timezone.now(), status=1)
    category_obj = Category.objects.all()
    cat_dict = {}
    for cat_name in category_obj:
        cat_dict[cat_name] = post_obj.filter(category_list=cat_name).count()
    return {'cat_dict': cat_dict}


@register.inclusion_tag('latest-post.html')
def latest_posts():
    post_obj = Post.objects.filter(published_date__lt=timezone.now(), status=1).order_by('-published_date')[:3]
    return {'post_obj': post_obj}

@register.inclusion_tag('blog_items/blog-tags.html')
def show_tags():
    post_obj = Post.objects.filter(published_date__lt=timezone.now(), status=1)
    return {'post_obj': post_obj}
