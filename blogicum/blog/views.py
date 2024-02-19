from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.utils import timezone as tz

from blog.models import Post, Category
from .constants import POSTS_IN_HOMEPAGE


def postfilter():
    return Post.objects.select_related(
        'category',
        'location',
        'author',
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=tz.now()
    )


def index(request):
    template = 'blog/index.html'
    post_list = postfilter()[:POSTS_IN_HOMEPAGE]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'blog/detail.html'
    post = get_object_or_404(
        postfilter(),
        pk=post_id
    )
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    posts = postfilter().filter(category=category)
    context = {'category': category, 'post_list': posts}
    return render(request, template, context)
