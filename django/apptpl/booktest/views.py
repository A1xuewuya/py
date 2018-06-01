# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from models import *


# Create your views here.

def index(request):
    # 根据主键查询一条数据
    # hero = HeroInfo.objects.get(pk=35)
    # list = HeroInfo.objects.filter(isDelete=True)  # 什么数据都没有
    list = HeroInfo.objects.filter(isDelete=False)
    context = dict(
        # hero=hero
        list=list
    )
    return render(request, 'booktest/index.html', context)


def show(request, id):
    context = dict(
        id=id
    )
    return render(request, 'booktest/show.html', context)


def index2(request):
    return render(request, 'booktest/index2.html')


def csrfTest1(request):
    return render(request, 'booktest/csrf1.html')


def csrfTest2(request):
    return render(request, 'booktest/csrf2.html')


# 验证码
def verifyCode(request):
    # 引入绘图模块
    from PIL import Image, ImageDraw, ImageFont
    import random
    # 创建背景色
    bgColor = (random.randrange(50, 100), random.randrange(50, 100), random.randrange(50, 100))
    # 设定宽高
    width = 100
    height = 25
    # 创建画布
    image = Image.new('RGB', (width, height), bgColor)
    # 创建字体
    font = ImageFont.truetype('ARLRDBD.TTF', 24)
    # 创建画笔
    draw = ImageDraw.Draw(image)
    # 创建文本内容
    text = 'ABCD'
    # 逐个绘制字符
    # 绘制文本
    draw.text((0, 0), text, (255, 255, 255), font)
    # 保存到内存流中
    import cStringIO
    buf = cStringIO.StringIO()
    image.save(buf, 'png')
    # 将内存中的内容输入到客户端
    return HttpResponse(buf.getvalue(), 'image/png')
