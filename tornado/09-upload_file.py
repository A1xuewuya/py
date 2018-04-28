#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 文件上传
import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import define, options

define("port", default=8000, type=int, help="run server on given port...")


class IndexHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        self.write("post...")


class UploadHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        # files = self.request.files["image1"][0]["body"]
        files = self.request.files
        img_files = files.get("img")
        if img_files:
            img_file = img_files[0]["body"]
            f = open("./file", "w+")
            f.write(img_file)
            f.close()
        self.write("ok")


if __name__ == '__main__':
    options.parse_command_line()
    app = tornado.web.Application([
        (r"/", IndexHandler),
        (r"/upload", UploadHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
