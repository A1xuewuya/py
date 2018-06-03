# -*- coding:utf-8 -*-
from handler import *
from django.shortcuts import render


# 注册页面渲染
def register(request):
    return render(request, 'df_user/register.html')


# 登录页面渲染
def login(request):
    return render(request, 'df_user/login.html')
