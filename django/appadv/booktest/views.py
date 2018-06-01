# -*- coding:utf-8 -*-

from handler import *
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.渲染界面

def index(request):
    return render(request, 'booktest/index.html')


def uploadPic(request):
    return render(request, 'booktest/uploadpic.html')


# def areainfo(request):
#     return render(request, 'booktest/areainfo.html')
