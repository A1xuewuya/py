# -*- coding:utf-8 -*-
#
import os
import json
import torndb
import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import define, options

define("port", default=8000, type=int, help="server port...")


class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        print("set headers...")
        # self.set_header("Content-Type", "application/json; charset=UTF-8")

    def initialize(self):
        pass

    def prepare(self):
        if self.request.headers.get("Content-Type", "").startswith("application/json"):
            self.json_dict = json.loads(self.request.body)
        else:
            self.json_dict = None

    def write_error(self, status_code, **kwargs):
        self.write("出错了，状态码是%s"%status_code)
        self.write("title: %s"% kwargs.get("err_title"))
        self.write("content: %s"% kwargs.get("err_con"))

    def on_finish(self):
        pass


class IndexHandler(BaseHandler):
    def get(self):
        self.write("index..get")

    def post(self, *args, **kwargs):
        err_data = {
            "err_title": "file error",
            "err_con": "wen jian wei ding yi"
        }
        self.send_error(404, **err_data)


class Application(tornado.web.Application):
    def __init__(self):
        urls = [
            (r"/", IndexHandler),
        ]

        settings = dict(
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            template_path=os.path.join(os.path.dirname(__file__), "template"),
            cookie_secret="vhtg1H+oQ3af5thzfFYWyOV2gCk+HUHKkgEbetKj/0c=",
            # xsrf_cookies=True,
            debug=True,
        )
        super(Application, self).__init__(handlers=urls, **settings)
        self.db = torndb.Connection(
            host="10.10.121.106",
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