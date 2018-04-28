# -*- coding:utf-8 -*-
# 接口及调用顺序
import json
import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import define, options

define("port", default=8000, type=int, help="server port...")


class IndexHandler(tornado.web.RequestHandler):
    def initialize(self):
        pass

    def prepare(self):
        if self.request.headers.get("Content-Type", "").startswith("application/json; charset=UTF-8"):
            self.json_dict = json.loads(self.request.body)
        else:
            self.json_dict = None

    def get(self, *args, **kwargs):
        self.write("get...")

    def post(self, *args, **kwargs):
        self.write("post...")


if __name__ == '__main__':
    app = tornado.web.Application([
        (r"/", IndexHandler)
    ], debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
