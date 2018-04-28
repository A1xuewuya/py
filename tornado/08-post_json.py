#!/usr/bin/env python
# -*- coding:utf-8 -*-
# get请求
# 获取查询字符串参数
import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
import json

tornado.options.define("port", default=8011, type=int, help="run server on the givrn port...")


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # self.write("get请求测试...")
        # 获取查询字符串参数
        res1 = self.get_query_argument("a", default=None)
        res2 = self.get_query_arguments('b')
        # self.write(res1+res2)
        self.write(res1)

    def post(self, *args, **kwargs):
        """传递json数据 json解析"""
        print(self.request)
        # 判断是否是json传输数据
        if self.request.headers.get("Content-Type") == "application/json":
            json_data = self.request.body
            """json解析"""
            json_args = json.loads(json_data)
            print(json_args)
            self.write(json_args)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    print(tornado.options.options.port)
    app = tornado.web.Application([
        (r"/", IndexHandler)
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()