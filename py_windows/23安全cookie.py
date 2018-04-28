# -*- coding:utf-8 -*-
#
import os
import json
import time
import datetime
import torndb
import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import define, options

define("port", default=8000, type=int, help="server port..")


class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        # self.set_header("Content-Type", "application/json; charset=UTF-8")
        # 设置headers头的server键值对
        self.set_header("Server", "nzc-server")
        pass

    def initialize(self):
        pass

    def prepare(self):
        if self.request.headers.get("Content-Type", "").startswith("application/json"):
            self.json_dict = json.loads(self.request.body)
        else:
            self.json_dict = None

    # def write_error(self, status_code, **kwargs):
    #     pass


class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        # 设置安全cookie
        self.set_secure_cookie("name-test", "value-test")
        # 获取设置的cookie
        cookie = self.get_secure_cookie("name-test", value=None)
        self.write(str(cookie))

    def post(self, *args, **kwargs):
        self.write("post..")


class Application(tornado.web.Application):
    def __init__(self):
        urls = [
            (r"/", IndexHandler),
        ]
        settings = dict(
            debug=True,
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            template_path=os.path.join(os.path.dirname(__file__), "template"),
            cookie_secret="USI6bZ9XSRuGGRfqhAHFfWzZXNbP+k8EgqGt4p8/hIc=",
        )
        super(Application, self).__init__(handlers=urls, **settings)
        self.db = torndb.Connection(
            host="127.0.0.1",
            database="pytest",
            user="root",
            password="root",
        )


if __name__ == '__main__':
    options.parse_command_line()
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
