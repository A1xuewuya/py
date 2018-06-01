# -*- coding:utf-8 -*-
from django.shortcuts import render
from models import *
from django.http import JsonResponse, HttpResponse
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from task import *


def index(request):
    return render(request, 'booktest/index.html')


def pro(request):
    prolist = AreaInfo.objects.filter(prea__isnull=True)
    list = []
    for item in prolist:
        list.append({item.id, item.title})
    resp = dict(
        data=list
    )
    return JsonResponse(resp)


# 缓存 单个view缓存
@cache_page(60 * 10)
def cache1(request):
    return HttpResponse("hello cache1")
    # return HttpResponse("hello cache2")


# 模板片断缓存
def cache2(request):
    return render(request, 'booktest/cache2.html')


# 缓存数据
def cache3(request):
    # cache.set("key1", "value1")
    res = cache.get("key1")
    print(res)


def cache4(request):
    return


def celeryTest(request):
    sayhello.delay()
    return HttpResponse("ok")