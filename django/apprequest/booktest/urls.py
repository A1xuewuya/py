#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^alllist/$', alllist),
    url(r'^getquery/$', getquery),
    url(r'^getlist/$', getlist),
    url(r'^post1/$', getPostTest1),
    url(r'^cookietest/$', cookieTest),
    url(r'^redtest1/$', redirectTest1),
    url(r'^redtest2/$', redirectTest2),
    url(r'^login/$', login),
    url(r'^login_handle/$', login_handle),
    url(r'^home/$', home),
    url(r'^loginout/$', loginout),
]
