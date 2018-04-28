# -*- coding:utf-8 -*-
# 重定向
import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import define, options

define("port", default=80, type=int, help="server port...")


class IndexHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.write("index_get...")

    def post(self, *args, **kwargs):
        self.write("index_post...")


class RedirectHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("..RedirectHandler")
        # 重定向到IndexHandler中去执行
        self.redirect("/")


if __name__ == '__main__':
    options.parse_command_line()
    app = tornado.web.Application([
        (r"/", IndexHandler),
        (r"/test", RedirectHandler)
    ], debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

