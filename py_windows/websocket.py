# -*- coding:utf-8 -*-
#
"""
实时获取消息
    1.前端论询(有无立即回复)  后端服务器 /api/order/new
    2.长论询 没有数据改变不做任何回应，当有数据改变时 服务器才回复响应
    3.websocket 长连接
"""
import tornado.websocket
import os
import json
import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import define, options

define("port", default=8000, type=int, help="server port..")


class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        # self.set_header("Content-Type", "application/json; charset=UTF-8")
        pass

    def prepare(self):
        if self.request.headers.get("Content-Type", "").startswith("application/json"):
            json_dict = json.loads(self.request.body)
        else:
            json_dict = None

    def write_error(self, status_code, **kwargs):
        self.write("<h1>错误了..</h1>")
        self.write("title: %s <br>" % kwargs.get("err_title", ""))
        self.write("con: %s <br>" % kwargs.get("err_con", ""))


class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.write("get..")

    def post(self, *args, **kwargs):
        self.send_error("post")


class ChatHandler(tornado.websocket.WebSocketHandler):
    # 类属性 用户websocket连接列表
    users = []

    # 当一个WebSocket连接建立后被调用
    def open(self, *args, **kwargs):
        for user in self.users:
            user.write_message("%s 上线了"% self.request.remote_ip)
        self.users.append(self)

    # 当客户端发送消息message过来时被调用，注意此方法必须被重写
    def on_message(self, message):
        for user in self.users:
            user.write_message("%s 说：%s" %(self.request.remote_ip, message))

    # 当WebSocket连接关闭后被调用
    def on_close(self):
        self.users.remove(self)
        self.write_message("%s 下线了"% self.request.remote_ip)

    def check_origin(self, origin):
        return True


if __name__ == '__main__':
    urls = [
        (r"/", IndexHandler),
        (r"/chat", ChatHandler),
        # tornado自带那的静态资源访问handler 传递一个字典  访问http://10.10.121.125:8000/index.html
        # 在字典中加上default_filename 访问http://10.10.121.125:8000/
        # 把这个放到最后
        (r"/(.*)", tornado.web.StaticFileHandler, {"path": os.path.join(
            os.path.dirname(__file__), "static/html"), "default_filename": "websocket.html"})
    ]
    settings = {
        # 设置是否调试模式
        "debug": "True",
        # 设置静态资源路径  访问http://10.10.121.125:8000/static/html/index.html
        "static_path": os.path.join(os.path.dirname(__file__), "static"),
    }
    app = tornado.web.Application(handlers=urls, **settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
