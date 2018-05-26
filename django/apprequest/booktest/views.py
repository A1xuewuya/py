# -*- coding:utf-8 -*-
#
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def index(request):
    return HttpResponse("index")


def alllist(request):
    return render(request, "booktest/alllist.html")


def getquery(request):
    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']
    return render(request, "booktest/getquery.html")


def getlist(request):
    a = request.GET.getlist('a')
    return render(request, "booktest/getlist.html")


# post接收数据
def getPostTest1(request):
    a = request.POST['a']
    context = dict(
        a=a
    )
    return render(request, 'booktest/posttest1.html', context)


# 测试cookie
def cookieTest(request):
    response = HttpResponse()
    # 获取cookie
    cookie = request.COOKIES
    if cookie.has_key('t1'):
        response.write(cookie['t1'])
    # response.set_cookie('t1','abc')
    return response


# 测试重定向
def redirectTest1(request):
    # return HttpResponseRedirect('/booktest/redtest2/')
    return redirect('/booktest/redtest2/')


def redirectTest2(request):
    return HttpResponse('这是重定向的页面')


# 测试session登陆
def login(request):
    return render(request, 'booktest/login.html')


def login_handle(request):
    username = request.POST.get('username')
    # 设置session
    request.session['username'] = username
    # 设置过期时间
    request.session.set_expiry(0)
    return redirect('/booktest/home/')


def home(request):
    username = request.session.get('username')
    if not username:
        return redirect('/booktest/login/')
    context = dict(
        username=username
    )
    return render(request,'booktest/home.html', context)


def loginout(request):
    request.session.clear()
    return redirect('/booktest/login/')
