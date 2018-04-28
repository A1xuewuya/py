#!/usr/bin/env python
# -*- coding:utf-8 -*-
# options
#
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

# 定义服务器监听端口选项
tornado.options.define("port", default=8000, type=int, help="port...")
# 无意义，演示多值情况
tornado.options.define("itcast", default=[], type=str, multiple=True, help="itcast subjects.")


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("get...")


if __name__ == '__main__':
    tornado.options.parse_config_file("./config")  # 仅仅修改了此处
    print tornado.options.options.itcast  # 输出多值选项
    app = tornado.web.Application([
        (r"/", IndexHandler)
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()

    """
    config文件
    port = 9000
    itcast = ["python", "c++", "java", "php", "ios"]
    """