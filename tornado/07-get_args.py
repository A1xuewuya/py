#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 获取查询字符串参数
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

tornado.options.define("port", default=8011, type=int, help="run server on the given port.")


class IndexHandler(tornado.web.RequestHandler):
    """主页处理类"""
    def get(self):
        """get请求方式"""
        subject = self.get_argument("subject", default="python")  # subject参数 默认为python（非必要参数）
        query_args = self.get_argument("q")  # 获取查询参数（必要参数）
        query_args = self.get_arguments("q")  # 获取查询参数，以列表形式返回（必要）
        self.write(query_args)

    def post(self, *args, **kwargs):
        """post请求方式"""
        # test = self.get_query_argument('q')
        # body_arg = self.get_body_argument("b")  # 获取请求体参数
        # body_args = self.get_body_arguments("b")
        # self.write(str(body_args))

        # 前两类方法的整合
        a = self.get_argument("a" , strip=True)
        # a = self.get_arguments("a")
        self.write(a)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    print(tornado.options.options.port)
    app = tornado.web.Application([
        (r"/", IndexHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()
