from django.http import HttpResponse
from django.shortcuts import render

def post_list(reguest):
    names = ['Alex', 'Lara', '*****', 'Megi']
    print(reguest)
    return render(reguest, 'blog/blog.html', context={'names' : names})