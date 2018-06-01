#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index),
    url(r'^pro$', views.pro),
    url(r'^cache1$', views.cache1),
    url(r'^cache2$', views.cache2),
    url(r'^cache3$', views.cache3),
    url(r'^celery$', views.celeryTest)
]
