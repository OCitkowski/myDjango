from django.http import HttpResponse
from django.shortcuts import render
from .models import Post, Tag

def post_list(reguest):
    # names = ['Alex', 'Lara', '*****', 'Megi']
    # print(reguest)
    # return render(reguest, 'blog/blog.html', context={'names' : names})
    posts = Post.objects.all()
    return render(reguest, 'blog/blog.html', context={'posts':posts} )

def post_detail(reguest, slug):

    post = Post.objects.get(slug__iexact=slug)
    return render(reguest, 'blog/post_detail.html', context={'post':post} )

def tag_detail(reguest, slug):

    tag = Tag.objects.get(slug__iexact=slug)
    return render(reguest, 'blog/tag_detail.html', context={'tag':tag} )

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags':tags})