# -*- coding:utf-8 -*-
# 获取输入 获取前端传进来的参数：
# 查询字符串（query string)，形如?key1=value1&key2=value2；
# 请求体（body）中发送的数据，比如表单数据、json、xml；
# 提取uri的特定部分，如/blogs/2016/09/0001，可以在服务器端的路由中用正则表达式截取；
# 在http报文的头（header）中增加自定义字段，如X-XSRFToken=itcast。
import json
import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import define, options

define("port", default=8000, type=int, help="server port...")


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("get...")

    def post(self, *args, **kwargs):
        res = self.request.headers.get("Content-Type")
        """获取json数据"""
        json_data = self.request.body
        """解析json，将数据解析为字典dict"""
        res = json.loads(json_data)
        self.write(str(res))


if __name__ == '__main__':
    options.parse_command_line()
    # debug，设置tornado是否工作在调试模式
    app = tornado.web.Application([
        (r"/", IndexHandler),
    ], debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
