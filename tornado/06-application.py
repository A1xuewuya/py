#!/usr/bin/env python
# -*- coding:utf-8 -*-
# application类详解
import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver


tornado.options.define("port", default=8000, type=int, help="run server on the given port.")


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        python_url = self.reverse_url("python_url")
        self.write('<a href="%s">itcast</a>' %
                   python_url)


class ItcastHandler(tornado.web.RequestHandler):
    def initialize(self, subject):
        self.subject = subject

    def get(self):
        self.write(self.subject)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application([
        (r"/", IndexHandler),
        (r"/cpp", ItcastHandler, {"subject": "c++"}),
        tornado.web.url(r"/python", ItcastHandler, {"subject": "python"}, name="python_url")
    ], debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8000)
    tornado.ioloop.IOLoop.current().start()
