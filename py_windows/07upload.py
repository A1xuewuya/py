# -*- coding:utf-8 -*-
# 上传文件

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


class UploadHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("get...")

    def post(self, *args, **kwargs):
        res = self.request.files.get("image1")
        print(type(self.request.files))
        print(self.request.files.keys())
        print(type(self.request.files.get("image1")))
        self.write("post..upload")


if __name__ == '__main__':
    options.parse_command_line()
    # debug，设置tornado是否工作在调试模式
    app = tornado.web.Application([
        (r"/", IndexHandler),
        (r"/upload", UploadHandler)
    ], debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
