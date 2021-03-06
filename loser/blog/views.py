from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Tag
from django.views.generic import View
from .utils import *
from .forms import *


def post_list(reguest):
    # names = ['Alex', 'Lara', '*****', 'Megi']
    # print(reguest)
    # return render(reguest, 'blog/blog.html', context={'names' : names})
    posts = Post.objects.all()
    return render(reguest, 'blog/blog.html', context={'posts': posts})


# def post_detail(reguest, slug):
#
#     post = Post.objects.get(slug__iexact=slug)
#     return render(reguest, 'blog/post_detail.html', context={'post':post} )

class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'
    # def get(self, reguest, slug):
    #     # post = Post.objects.get(slug__iexact=slug)
    #     post = get_object_or_404(Post, slug__iexact=slug)
    #     return render(reguest, 'blog/post_detail.html', context={'post': post})


class PostCreate(ObjectCreateMixin, View):
    # def get(self, request):
    #     form = PostForm()
    #     return render(request, 'blog/post_create_form.html', context={'form': form})
    #
    # def post(self, request):
    #     bound_form = PostForm(request.POST)
    #
    #     if bound_form.is_valid():
    #         new_post = bound_form.save()
    #         return redirect(new_post)
    #     return render(request, 'blog/post_create_form.html', context={'form': bound_form})
    form_model = PostForm
    template = 'blog/post_create_form.html'


# def tag_detail(reguest, slug):
#
#     tag = Tag.objects.get(slug__iexact=slug)
#     return render(reguest, 'blog/tag_detail.html', context={'tag':tag} )

class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'

    # def get(self, reguest, slug):
    #     # tag = Tag.objects.get(slug__iexact=slug)
    #     tag = get_object_or_404(Tag, slug__iexact=slug)
    #     return render(reguest, 'blog/tag_detail.html', context={'tag': tag})


class TagCreate(ObjectCreateMixin, View):
    # def get(self, request):
    #     form = TagForm()
    #     return render(request, 'blog/tag_create.html', context={'form': form})
    #
    # def post(self, request):
    #     bound_form = TagForm(request.POST)
    #
    #     if bound_form.is_valid():
    #         new_tag = bound_form.save()
    #         return redirect(new_tag)
    #     return render(request, 'blog/tag_create.html', context={'form': bound_form})
    form_model = TagForm
    template = 'blog/tag_create.html'


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})
