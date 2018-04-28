# -*- coding:utf-8 -*-
#
import os
import json
import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import define, options

define("port", default=8000, type=int, help="server port..")


class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        # self.set_header("Content-Type", "application/json; charset=UTF-8")
        pass

    def prepare(self):
        if self.request.headers.get("Content-Type", "").startswith("application/json"):
            json_dict = json.loads(self.request.body)
        else:
            json_dict = None

    def write_error(self, status_code, **kwargs):
        self.write("<h1>错误了..</h1>")
        self.write("title: %s <br>" % kwargs.get("err_title", ""))
        self.write("con: %s <br>" % kwargs.get("err_con", ""))


class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        # 渲染模板
        # self.render("index.html", abc="abcdf")
        self.render("index.html", price1=1000, price2=2000)

    def post(self, *args, **kwargs):
        self.send_error(404, err_title="fdf", err_con="fff")


if __name__ == '__main__':
    urls = [
        (r"/", IndexHandler)
    ]
    settings = {
        "debug": "True",
        "static_path": os.path.join(os.path.dirname(__file__), "static"),
        # 模板路径
        "template_path": os.path.join(os.path.dirname(__file__), "template"),
    }
    app = tornado.web.Application(handlers=urls, **settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
