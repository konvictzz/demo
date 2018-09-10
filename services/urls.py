"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'services'
urlpatterns = [
    url(r'^url/$',views.UrlView.as_view(), name='url'),
    url(r'^url/(?P<pk>[0-9]+)/$', views.UrlDetailView.as_view(), name='url_detail'),
    url(r'^url/environment/(?P<pk>[0-9]+)/$',views.Environment_typeView.as_view(), name='environment'),
    url(r'^elasticsearchinfo/$', views.ElasticsearchView.as_view(), name='elasticsearchinfo'),
    url(r'^search/$', views.search, name='search'),
]
