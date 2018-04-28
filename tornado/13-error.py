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
    """设置默认字符集"""
    def set_default_headers(self):
        # self.set_header("Content-Type", "application/json; charset=UTF-8")
        pass

    """设置返回错误信息"""
    def write_error(self, status_code, **kwargs):
        """返回(抛出来)的错误信息必须包括：错误标题，错误描述"""
        self.write("出错了<br/>")
        self.write("错误标题: %s <br/>" % kwargs.get("error_title", "None"))
        self.write("错误描述: %s <br/>" % kwargs.get("error_content", "None"))


    def get(self, *args, **kwargs):
        # 返回错误状态码 之后不再执行 1
        # self.send_error(404, error_title="没找到标题...", error_content="没找到内容...")
        # 返回错误状态码 之后不再执行 2
        error_data = {
            "error_title": "title_test...",
            "error_content": "content_test..."
        }
        self.send_error(404, **error_data)
        self.write("get...index")

    def post(self, *args, **kwargs):
        self.write("post...index")


if __name__ == '__main__':
    options.parse_command_line()
    app = tornado.web.Application([
        (r"/", IndexHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
