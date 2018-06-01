#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
import views

from django.conf.urls import url

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^(\d+)', views.show, name='show'),
    url(r'^index2$', views.index2, name='index2'),
    url(r'^csrf1$', views.csrfTest1),
    url(r'^csrf2$', views.csrfTest2),
    url(r'^verify', views.verifyCode)
]
