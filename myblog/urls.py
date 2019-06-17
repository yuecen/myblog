"""myblog URL Configuration

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
from django.urls import path, include
from django.views.generic import RedirectView

from users.views import LoginView, logout, AboutMeView
from posts.views import PostListCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='blog/', permanent=False), name='index'),
    path('blog/', PostListCreateView.as_view(), name='blog_list'),
    path('roundup/',PostListCreateView.as_view(), name='roundup_list'),
    path('blog/', include('posts.urls')),
    path('roundup/', include('posts.urls')),
    path('login/', LoginView.as_view(), name='login_view'),
    path('logout/', logout, name='logout_view'),
    path('about_me/', AboutMeView.as_view(), name='about_me_view'),
]
