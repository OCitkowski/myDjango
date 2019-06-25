"""loser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from .views import redirect_blog

def hello(request):
    return HttpResponse("Hello, world. You're at the polls index.")

urlpatterns = [
    # path('', hello),

    # path('admin/logout/', redirect_blog),
    path('', redirect_blog),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]

