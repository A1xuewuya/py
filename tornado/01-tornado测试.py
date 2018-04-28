#!/usr/bin/env python
# -*- coding:utf-8 -*-
# tornado测试
import tornado.web
import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):
    """主页处理类"""
    def get(self, *args, **kwargs):
        """get请求方式"""
        self.write('get...')

    def post(self, *args, **kwargs):
        self.write('post...')


if __name__ == '__main__':
    app = tornado.web.Application([(r"/", IndexHandler)])
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
