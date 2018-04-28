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
    # 回调异步
    """
    @tornado.web.asynchronous
    def get(self, *args, **kwargs):
        client = AsyncHTTPClient()
        client.fetch("http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip=117.158.83.66", callback=self.on_response)

    def on_response(self, resp):
        if resp.error:
            self.write(500)
        else:
            data = json.loads(resp.body)
            if data["ret"] == 1:
                self.write(u"国家:%s，省份:%s , 城市:%s"%(data['country'], data['province'], data['city']))
            else:
                self.write("ip查询错误")
        self.finish()
        """

    # 协程异步
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        http = AsyncHTTPClient()
        resp = yield http.fetch("http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip=117.158.83.66")
        if resp.error:
            self.send_error(500)
        else:
            data = json.loads(resp.body)
            if data.get("ret", "") == 1:
                self.write(data)
            else:
                self.write("ip查询信息错误")


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
