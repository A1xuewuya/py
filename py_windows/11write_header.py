# -*- coding:utf-8 -*-
#
import json
import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import define, options

define("port", default=80, type=int, help="server port...")


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # 手动json序列化
        stu = {
            "name": "wt",
            "age": 22
        }
        res = json.dumps(stu)
        # self.write(res)

        # write方法默认会进行序列化，设置header   推荐用这种方式穿字符串和字典
        stu = {
            "name": "wt",
            "age": 22
        }
        # application/json;charset=UTF-8
        self.write(stu)

    def post(self, *args, **kwargs):
        """设置content-type类型，可以自定义"""
        self.set_header("Content-Type", "text/html")
        self.set_header("test-key", "test-value")
        self.write("ok")


if __name__ == '__main__':
    options.parse_command_line()
    app = tornado.web.Application([
        (r"/", IndexHandler),
    ], debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

