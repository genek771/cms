from django.http import Http404
from django.shortcuts import render
from django.views import View

from .models import Post, Comment


class PostList(View):
    def get(self, request):
        posts = Post.objects.filter(category__active=True)
        return render(request, 'blog/post-list.html', {"post_list": posts})


class PostCategory(View):
    def get(self, request, category):
        posts = Post.objects.filter(category__slug=category, category__active=True)
        if posts.exists():
            return render(request, 'blog/post-list.html', {"post_list": posts})
        else:
            raise Http404