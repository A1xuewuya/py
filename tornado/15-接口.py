#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 代码错误 字符编码
import json
import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import define, options

define("port", default=8000, type=int, help="server port...")


class IndexHnadler(tornado.web.RequestHandler):
    def prepare(self):
        if self.request.headers.get("Content-Type", "").startswith("application/json"):
            self.json_dict = json.loads(self.request.body)
        else:
            self.json_dict = None

    def get(self, *args, **kwargs):
        self.write("get...")

    def post(self, *args, **kwargs):
        if self.json_dict:
            for key, value in self.json_dict.items():
                self.write("<h3>%s</h3><p>%s</p>" % (key, value))


if __name__ == '__main__':
    options.parse_command_line()
    app = tornado.web.Application([
        (r"/", IndexHnadler),
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()