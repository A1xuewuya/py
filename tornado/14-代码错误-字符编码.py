#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 代码错误 字符编码
import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import define, options

define("port", default=8000, type=int, help="server port...")


class IndexHnadler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        self.write("post...")


class LoginHandler(tornado.web.RequestHandler):
    def write_error(self, status_code, **kwargs):
        self.write("<h1>程序员GG正在赶来...</h1>")
        self.write("title:%s <br>" % kwargs.get("error_title"))
        self.write("content:%s <br>" % kwargs.get("error_content"))
        # self.write(u"title:%s <br>" % kwargs["error_title"])
        # self.write(u"content:%s <br>" % kwargs["error_content"])

    def get(self, *args, **kwargs):
        code = self.get_argument("code", default=None)
        title = self.get_argument("title", default="")
        content = self.get_argument("content", default="")
        if code:
            self.send_error(int(code), error_title=title, error_content=content)
        else:
            self.write("主页...")

        error_data = {
            "error_title": "错误标题。。。",
            "error_content": "错误内容。。。"
        }
        # self.send_error(404, **error_data)
        # self.write("login...")


if __name__ == '__main__':
    options.parse_command_line()
    app = tornado.web.Application([
        (r"/", IndexHnadler),
        (r"/login", LoginHandler)
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()