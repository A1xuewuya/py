# -*- coding:utf-8 -*-
# 数据库操作 增删改查
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
        self.set_header("Server", "server")
        # self.set_header("Content-type", "application/json; charset=utf-8")

    def initialize(self):
        pass

    def prepare(self):
        if self.request.headers.get("Content-Type", "").startswith("application/json"):
            self.json_dict = json.loads(self.request.body)
        else:
            self.json_dict = None

    """
    def write_error(self, status_code, **kwargs):
        self.write("出错了: %s <br>" % status_code)
        self.write("title: %s" % kwargs.get("err_title", ""))
        self.write("content: %s" % kwargs.get("err_con", ""))
    """

    """
    def on_finish(self):
        pass
    """


class IndexHandler(BaseHandler):
    def get(self):
        self.write("index...get")

    def post(self, *args, **kwargs):
        self.write("index...post")


class InsertHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.write("select..get")

    def post(self, *args, **kwargs):
        name = self.get_argument("name", strip=True)
        if name is not None:
            try:
                self.application.db.execute("insert into userinfo(name) values(%s)" % name)
            except Exception as e:
                self.write("db error: %s" % e)
            else:
                self.write("添加成功")


class DeleteHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.write("select..get")

    def post(self, *args, **kwargs):
        self.application.db.execute("delete from userinfo where name=2")
        # self.write("select..post")


class SelectHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.write("select..get")

    def post(self, *args, **kwargs):
        self.write("select..post")


class Application(tornado.web.Application):
    def __init__(self):
        urls = [
            (r"/", IndexHandler),
            (r"/api/db/select", SelectHandler),
            (r"/api/db/insert", InsertHandler),
            (r"/api/db/delete", DeleteHandler),
            (r"/api/db/select", SelectHandler)
        ]
        settings = dict(
            static_path=os.path.join(os.path.dirname(__file__), "statics"),
            template_path=os.path.join(os.path.dirname(__file__), "template"),
            secret_cookie="U9HLvQXQRtuwEy+Tw3Np1LQm6PKO1EnalupWgkocPJU=",
            login_url="/login",
            # xsrf_cookies=True,
            debug=True,
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



