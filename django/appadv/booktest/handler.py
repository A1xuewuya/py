#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from models import *
from django.core.paginator import *


def upload_handle(request):
    file = request.FILES['pic']
    fname = '%s%s' % (settings.MEDIA_ROOT, file.name)
    with open(fname, 'w') as pic:
        for c in file.chunks():
            pic.write(c)
    return HttpResponse('ok')


# 进行分页练习
def hero_list(request, pindex):
    if pindex == '':
        pindex = 1
    # 获取所有数据集合
    list = HeroInfo.objects.all()
    # 创建paginator对象
    paginator = Paginator(list, 5)
    # 拿到具体某一页
    page = paginator.page(int(pindex))
    context = dict(
        page=page
    )
    return render(request, 'booktest/herolist.html', context)


# 获取省市信息
def areainfo(request):
    get = request.GET
    id = int(get.get('id'))
    if id == 0:
        # data = AreaInfo.objects.filter(parea__isnull=True).values()
        data = AreaInfo.objects.filter(parea__isnull=True)
    else:
        data = [{}]
    list = []
    for a in data:
        list.append([a.id, a.title])
    resp = dict(
        data=list
    )
    return JsonResponse(resp)