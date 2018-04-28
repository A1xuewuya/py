# -*- coding:utf-8 -*-
# 获取输入 获取前端传进来的参数：
# 查询字符串（query string)，形如?key1=value1&key2=value2；
# 请求体（body）中发送的数据，比如表单数据、json、xml；
# 提取uri的特定部分，如/blogs/2016/09/0001，可以在服务器端的路由中用正则表达式截取；
# 在http报文的头（header）中增加自定义字段，如X-XSRFToken=itcast。
import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import define, options

define("port", default=8000, type=int, help="server port...")


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        a = self.get_query_argument("a")
        b = self.get_query_argument("b")
        self.write(a + b)

    def post(self, *args, **kwargs):
        a = self.get_body_argument("a", default=None)
        b = self.get_body_argument("b", default=None)
        c = self.get_argument("c", default=None, strip=True)
        self.write(a+b)


if __name__ == '__main__':
    options.parse_command_line()
    # debug，设置tornado是否工作在调试模式
    app = tornado.web.Application([
        (r"/", IndexHandler),
    ], debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
