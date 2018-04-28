#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
import tornado.web
import tornado.ioloop
import tornado.httpserver
import json
from tornado.options import options, define

define("port", default=8000, type=int, help="run server on given port...")


class IndexHnadler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type", "application/json; charset=UTF-8")

    def get(self, *args, **kwargs):
        stu = {
            "name": "wt",
            "age": 22,
        }
        # stu = json.dumps(stu)
        # self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.write(stu)

    def post(self, *args, **kwargs):
        stu = {
            "name": "wt",
            "age": 22,
        }
        self.request.body
        # 第一种方式 ，自己手动设置返回头
        # self.set_header("Content-Type", "application/json; charset=UTF-8")
        res = json.dumps(stu)
        self.write(res)


if __name__ == '__main__':
    options.parse_command_line()
    app = tornado.web.Application([
        (r"/", IndexHnadler)
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
