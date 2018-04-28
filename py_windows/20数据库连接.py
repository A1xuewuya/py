# -*- coding:utf-8 -*-
#
import os
import json
import tornado.web
import tornado.ioloop
import tornado.httpserver
import torndb
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
        res = self.application.db.get("SELECT * FROM userinfo WHERE id=2")
        print(type(res))
        print(res)
        self.write(res)

    def post(self, *args, **kwargs):
        self.send_error(404, err_title="fdf", err_con="fff")


class Application(tornado.web.Application):
    def __init__(self):
        urls = [
            (r"/", IndexHandler),
        ]
        settings = dict(
            debug="True",
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            template_path=os.path.join(os.path.dirname(__file__), "template"),
        )
        # 重载父类application
        super(Application, self).__init__(handlers=urls, **settings)
        # 创建一个全局mysql连接实例供handler使用
        self.db = torndb.Connection(
            host="127.0.0.1",
            database="pytest",
            user="root",
            password="root"
        )


if __name__ == '__main__':
    options.parse_command_line()
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
