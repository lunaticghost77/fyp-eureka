"""FinalYearProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from eureka import views

urlpatterns = [
    url(r'^0309526', include(admin.site.urls)),
    url(r'^$', views.index),
    url(r'^index$', views.welcome, name='welcome'),
    url(r'^about$', views.showAboutPage, name='aboutpage'),
    url(r'^howitworks$', views.showHowWorks, name='howpage'),
    url(r'^explore$', views.showExplore, name='explore'),
    url(r'^start$', views.startProject, name='startproj'),
]
