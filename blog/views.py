from django.shortcuts import render


# Create your views here.
def list_view(request):
    return render(request, 'blog_items/blog-list.html')


def single_view(request):
    return render(request, 'blog_items/blog-single.html')
