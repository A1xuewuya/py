#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
import views
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', views.index),
]
