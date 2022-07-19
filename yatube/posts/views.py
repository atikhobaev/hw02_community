from django.shortcuts import render, get_object_or_404

from .models import Post, Group

post_quantity = 10


def index(request):
    """Главная страница с постами."""
    posts = Post.objects.all()[:post_quantity]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    """Страница группы с постами."""
    group = get_object_or_404(Group, slug=slug)

    posts = (group.posts.all()[:post_quantity])
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
