# -*- coding:utf-8 -*-
#
"""
将Application的设置参数（目前只学习了debug）抽离为一个字典类型变量settings，并在构造Application对象时使用settings。

熟练使用RequestHandler的各种输入输出方法。

尝试抽象出BaseHandler基类，继承自RequestHandler，并在此基类中实现prepare（解析json数据）、write_error两个接口。
"""
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
        self.write("index..get")

    def post(self, *args, **kwargs):
        self.send_error(404, err_title="fdf", err_con="fff")


if __name__ == '__main__':
    urls = [
        (r"/", IndexHandler),
    ]
    settings = {
        "debug": "True",
    }
    app = tornado.web.Application(handlers=urls, **settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
