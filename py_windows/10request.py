# -*- coding:utf-8 -*-
#
import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import define, options
"""
RequestHandler.request 对象存储了关于请求的相关信息，具体属性有：

method HTTP的请求方式，如GET或POST;
host 被请求的主机名；
uri 请求的完整资源标示，包括路径和查询字符串；
path 请求的路径部分；
query 请求的查询字符串部分；
version 使用的HTTP版本；
headers 请求的协议头，是类字典型的对象，支持关键字索引的方式获取特定协议头信息，例如：request.headers["Content-Type"]
body 请求体数据；
remote_ip 客户端的IP地址；
files 用户上传的文件，为字典类型，型如：
"""

define("port", default=80, type=int, help="server port...")


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("请求方式:%s <br>" % self.request.method)
        self.write("客户端ip:%s" % self.request.remote_ip)


if __name__ == '__main__':
    app = tornado.web.Application([
        (r"/", IndexHandler),
    ], debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
