#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
import views
from django.conf.urls import url

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^uploadpic/$', views.uploadPic),
    url(r'^upload_handle/$', views.upload_handle),
    url(r'^herolist/(\d*)$', views.hero_list),
    url(r'^areainfo/$', views.areainfo)
]
