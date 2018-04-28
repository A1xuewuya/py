#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.web
import tornado.ioloop
import tornado.httpserver


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("get请求...(tornado)")


if __name__ == '__main__':
    app = tornado.web.Application([
        (r"/", IndexHandler)
    ])
    # app.listen(8000)
    # 修改部分
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8000)
    tornado.ioloop.IOLoop.current().start()