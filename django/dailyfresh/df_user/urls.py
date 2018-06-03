#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
import views

from django.conf.urls import url

urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^register_exist/$', views.register_exist),
    url(r'^register_handle/$', views.register_handle),
    url(r'^login/$', views.login),
    url(r'^login_handle/$', views.login_handle),
    url(r'^info/$', views)
]
