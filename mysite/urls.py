"""mysite URL Configuration

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
from django.contrib.flatpages import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('blog/', include('blog.urls')),
    path('infopages/about/', views.flatpage, {'url': 'infopages/about/'}, name='about_index'),
    path('infopages/resume/', views.flatpage, {'url': 'infopages/resume/'}, name='resume_index'),
    path('infopages/contact/', views.flatpage, {'url': 'infopages/contact/'}, name='contact_index'),
    path('accounts/', include('accounts.urls')),
    path('users/', include('allauth.urls'))
]

