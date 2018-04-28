# -*- coding:utf-8 -*-
#
import json
import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import define, options

define("port", default=80, type=int, help="server port...")


class IndexHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        # self.set_header("test-key", "test-value")

    def get(self, *args, **kwargs):
        stu = {
            "name": "wt",
            "age": 22
        }
        res = json.dumps(stu)
        self.write(res)

    def post(self, *args, **kwargs):
        self.write("post...")


if __name__ == '__main__':
    options.parse_command_line()
    app = tornado.web.Application([
        (r"/", IndexHandler),
    ], debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
