# -*- coding:utf-8 -*-
#
import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import define, options

define("port", default=80, type=int, help="server port...")


class IndexHandler(tornado.web.RequestHandler):
    def write_error(self, status_code, **kwargs):
        """
        错误信息必须要包括：错误标题，错误描述
        """
        self.write("错误标题：%s <br>" % kwargs.get("err_title"))
        self.write("错误描述：%s <br>" % kwargs.get("err_con"))

    def get(self, *args, **kwargs):
        # 返回错误代码 抛出错误
        # 1...
        # self.send_error(404, err_title="abc...title", err_con="abc...con")
        # 2...
        err_data = {
            "err_title": "fff",
            "err_con": "ccc"
        }
        # 传递字典参数在前面加**,解包字典
        self.send_error(404, **err_data)
        # self.write("index_get...")

    def post(self, *args, **kwargs):
        self.write("index_post...")


if __name__ == '__main__':
    options.parse_command_line()
    app = tornado.web.Application([
        (r"/", IndexHandler),
    ], debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

