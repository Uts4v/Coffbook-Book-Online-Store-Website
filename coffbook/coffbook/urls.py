
"""Coffbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from myapp import views

admin.site.site_header="CoffBook Admin"
admin.site.site_title="Welcome to CoffBook"
admin.site.index_title="CoffBook Database"

urlpatterns = [
    # Page Redirects
    path('', views.home),
    path('home/', views.home),
    path('book/', views.book),
    path('service/', views.service),
    path('login/', views.login),
    path('register/', views.register),
    path('admin/', admin.site.urls),

    # Function
    path('home/', views.home),
    path('userRegister/', views.userRegister),
    path('contact/', views.contact),
    path('hello/', views.userRegister),
    path('loginCheck/', views.loginCheck),

    path('home/',views.home, name='event'),
]
