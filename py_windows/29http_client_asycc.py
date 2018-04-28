# -*- coding:utf-8 -*-
#
import os
import json
import tornado.web
import tornado.ioloop
import tornado.httpserver
import torndb
import tornado.gen
from tornado.options import define, options
from tornado.httpclient import AsyncHTTPClient

define("port", default=8000, type=int, help="server port..")


class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        # pass

    def prepare(self):
        if self.request.headers.get("Content-Type", "").startswith("application/json"):
            json_dict = json.loads(self.request.body)
        else:
            json_dict = None

    # def write_error(self, status_code, **kwargs):
    #     self.write("<h1>错误了..</h1>")
    #     self.write("title: %s <br>" % kwargs.get("err_title", ""))
    #     self.write("con: %s <br>" % kwargs.get("err_con", ""))


class IndexHandler(BaseHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        rep = yield self.get_ip_info("47.94.136.135")
        if rep['ret'] == 1:
            self.write(rep)
        else:
            self.write("查询信息错误")

    @tornado.gen.coroutine
    def get_ip_info(self, ip):
        http = AsyncHTTPClient()
        resp = yield http.fetch("http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip=" + ip)
        if resp.error:
            rep = {"ret":0}
        else:
            rep = json.loads(resp.body)
        raise tornado.gen.Return(rep)


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


if __name__ == '__main__':
    options.parse_command_line()
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
