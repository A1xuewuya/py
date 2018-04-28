#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#
import json
import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import define, options

define("port", default=8000, type=int, help="port...")


class IndexHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type", "application/json; charset=UTF-8")

    def get(self, *args, **kwargs):
        # 设置Header
        self.set_header("key-test", "value-test")
        # 设置状态码
        self.set_status(268, "status...test")
        self.set_status(222, "fdfds")
        self.write("hello...1")

    def post(self, *args, **kwargs):
        stu = {
            "grade": 1
        }
        res = json.loads(self.request.body)
        self.write(res)


if __name__ == '__main__':
    options.parse_command_line()
    app = tornado.web.Application([
        (r"/", IndexHandler)
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
