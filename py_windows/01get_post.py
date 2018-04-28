# -*- coding:utf-8 -*-
# 基础 get,post请求，，，
import tornado.web
import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):
    """对应http的get请求"""
    # def get(self, *args, **kwargs):
    #     self.write("get...")

    """对应http的post请求"""
    def get(self, *args, **kwargs):
        self.write("post...")


if __name__ == '__main__':
    app = tornado.web.Application([
        (r"/", IndexHandler)
    ])
    app.listen(8011)
    tornado.ioloop.IOLoop.current().start()
