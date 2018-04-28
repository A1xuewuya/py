# -*- coding:utf-8 -*-
# 正则表达式获取url参数

import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import define, options

define("port", default=8000, type=int, help="server port...")


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("get...")

    def post(self, *args, **kwargs):
        self.write()


if __name__ == '__main__':
    options.parse_command_line()
    # debug，设置tornado是否工作在调试模式
    app = tornado.web.Application([
        (r"/", IndexHandler),
    ], debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
