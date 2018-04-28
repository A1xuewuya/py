# -*- coding:utf-8 -*-
# 用户验证的机制 装饰器
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
        self.set_header("Server", "nzc_server")
        # self.set_header("Content-Type", "application/json; charset=UTF-8")

    def initialize(self):
        pass

    def prepare(self):
        if self.request.headers.get("Content-Type", "").startswith("application/json"):
            self.json_dict = json.loads(self.request.body)
        else:
            self.json_dict = None

    # def write_error(self, status_code, **kwargs):
    #     self.write("请求错误.")
    #     self.write("")
    #     self.write("")

    def on_finish(self):
        pass

    # 重写的requestHandler的方法
    def get_current_user(self):
        # 进行用户验证操作 可以用session进行用户状态：放到内存、缓存里面
        # 返回True False
        a = self.get_argument("a", default=None)
        if a:
            return True
        else:
            return False


class IndexHanler(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.write("这是个人主页.....")

    def post(self, *args, **kwargs):
        self.write("post")


class LoginHandler(BaseHandler):
    def get(self):
        next_url = self.get_argument("next", "")
        if next_url:
            # 跳转到用户验证后的网页
            self.redirect(next_url + "?a=login")
        else:
            self.write("you shoule login")


class Application(tornado.web.Application):
    def __init__(self):
        # 路由参数
        urls = [
            (r"/", IndexHanler),
            (r"/login", LoginHandler)
        ]
        # 配置参数
        settings = dict(
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            template_path=os.path.join(os.path.dirname(__file__), "template"),
            cookie_secret="U9HLvQXQRtuwEy+Tw3Np1LQm6PKO1EnalupWgkocPJU=",
            # xsrf_cookies=True,
            login_url="/login",
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
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()