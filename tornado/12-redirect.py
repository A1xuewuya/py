#!/usr/bin/env python
# -*- coding:utf-8 -*-
#

import tornado.web
import tornado.ioloop
import tornado.httpserver
import json
from tornado.options import options, define

define("port", default=8000, type=int, help="server port...")


class IndexHandler(tornado.web.RequestHandler):
    """主页处理类"""
    def set_default_headers(self):
        self.set_header("Content-Type", "application/json; charset=UTF-8")

    def get(self, *args, **kwargs):
        self.write("get...index")

    def post(self, *args, **kwargs):
        self.write("post...index")


class LoginHandler(tornado.web.RequestHandler):
    """登录类"""
    def set_default_headers(self):
        # self.set_header("Content-Type", "application/json; charset=UTF-8")
        pass

    def get(self, *args, **kwargs):
        self.write('<form method="post"><input type="submit" value="登陆"></form>')

    def post(self, *args, **kwargs):
        self.redirect("/")


if __name__ == '__main__':
    options.parse_command_line()
    app = tornado.web.Application([
        (r"/", IndexHandler),
        (r"/login", LoginHandler)
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
