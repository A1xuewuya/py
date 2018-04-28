# -*- coding:utf-8 -*-
# application详解
import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import define, options

define("port", default=8000, type=int, help="server port...")


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("你好世界，这是一个get...")

    def post(self, *args, **kwargs):
        self.write("你好世界,这是一个post...")


class testHandler(tornado.web.RequestHandler):
    def initialize(self, subject):
        self.subject = subject

    def post(self, *args, **kwargs):
        self.write(self.subject)


if __name__ == '__main__':
    options.parse_command_line()
    # debug，设置tornado是否工作在调试模式
    app = tornado.web.Application([
        (r"/", IndexHandler),
        (r"/test", testHandler, {"subject": "python"})
    ], debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
