#!/usr/bin/env python
# -*- coding:utf-8 -*-
from wsgiref.simple_server import make_server

def application(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])
    # return '<h1>Hello %s!<h2>' % (environ['PATH_INFO'] or 'web')
    f = open('news.html','r')
    con = f .read()
    return con

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print '接收http请求，端口8000...'

# 开始监听HTTP请求
httpd.serve_forever()

