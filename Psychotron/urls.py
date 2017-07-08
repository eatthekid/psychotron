"""Psychotron URL Configuration

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
# from django.contrib import admin
from main_app.views import *
from admin_app.views import *
from tests_app.views import *

urlpatterns = [
    url(r'^$', index),
]

urlpatterns += [
    url(r'^admin/$', admin,),
    url(r'^admin/delete/user/(\d+)$', delete_user),
    url(r'^admin/get_user_form/(\d+)$', get_user_form),
    url(r'^admin/create/user/(\d*)$', create_user),
    url(r'^profile/$', profile),
    url(r'^profile/edit/$', editProfile),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^registration/$', registration),
    url(r'^tests/$', tests),
    url(r'^tests/EPI/$', EPI_testing),
]