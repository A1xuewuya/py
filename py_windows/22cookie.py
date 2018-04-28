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
        # sql = "select * from userinfo"
        # res = self.application.db.query(sql)
        # self.write(str(res))
        # 设置cookie  设置有效时间为两天
        # self.set_cookie("name-test", "value-test", expires_days=2)
        # 设置过期时间为..
        self.set_cookie("aa", "bb", expires=time.strptime("2018-3-16 23:59:59", "%Y-%m-%d %H:%M:%S"))
        cookie = self.get_cookie("aa", default=None)
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
