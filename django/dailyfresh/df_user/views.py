# -*- coding:utf-8 -*-

from django.shortcuts import render, redirect
from models import *
from hashlib import sha1
from django.http import JsonResponse, HttpResponseRedirect


# 注册页面渲染
def register(request):
    return render(request, 'df_user/register.html')


# 注册时用户名是否存在处理
def register_exist(request):
    uname = request.GET.get('user_name')
    count = UserInfo.objects.filter(uname=uname).count()
    resp = dict(
        count=count
    )
    return JsonResponse(resp)


# 注册处理
def register_handle(request):
    # 接受用户输入
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    ucpwd = post.get('cpwd')
    uemail = post.get('email')
    # 参数校验
    if upwd != ucpwd:
        return redirect('/user/register/')
    # 数据处理 密码加密
    s1 = sha1()
    s1.update(upwd)
    upwd_f = s1.hexdigest()
    # 创建存储对象
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd_f
    user.uemail = uemail
    user.save()
    # 注册成功 转到登录页面
    return redirect('/user/login/')


# 登录页面渲染
def login(request):
    return render(request, 'df_user/login.html')


# 登录处理
def login_handle(request):
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    # 默认记住用户名值为1
    jizhu = post.get('jizhu', 0)
    # 根据用户名查询对象
    user = UserInfo.objects.filter(uname=uname)
    # 判断 如果未查到用户名则返回错误， 如果查到则判断密码是否正确，正确则转到用户中心
    if len(user) == 1:
        s = sha1()
        s.update(upwd)
        if s.hexdigest() == user[0].upwd:
            red = HttpResponseRedirect('/user/info/')
            # 记住用户名
            if jizhu != 0:
                red.set_cookie('uname', uname)
            else:
                red.set_cookie('uname', '', max_age=-1)
            request.session['user_name'] = uname
            request.session['user_id'] = user[0].id
            return red
        else:
            return render(request, 'df_user/login.html')
    else:
        context = dict(
            title="用户登录",
            error_name=0,
            error_pwd=1,
        )
        return render(request, 'df_user/login.html')