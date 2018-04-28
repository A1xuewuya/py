# -*- coding:utf-8 -*-
#
import os
import json
import tornado.web
import tornado.ioloop
import tornado.httpserver
import torndb
from tornado.options import define, options

define("port", default=8000, type=int, help="server port..")


class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        # pass

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
        # execute(query, parameters, *kwparameters) 返回影响的最后一条自增字段值
        # execute_rowcount(query, parameters, *kwparameters)  返回影响的行数
        # res = self.application.db.execute("insert into userinfo(name) values('aa')")
        res = self.application.db.execute("insert into userinfo(name) values(%s)", "你好")
        self.write(str(res))

    def post(self, *args, **kwargs):
        # 获取用户信息
        name = self.get_argument("name", strip=True)
        sql = "insert into userinfo(name) values(%s)"
        try:
            userid = self.application.db.execute(sql, name)
        except Exception as e:
            print(e)
            self.write("db error: %s" % e)
        self.write(str(userid))


class QueryHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.write("get...")

    def post(self, *args, **kwargs):
        sql = "select * from userinfo"
        try:
            rows = self.application.db.query(sql)
        except Exception as e:
            self.write({"error": 1, "error_msg": "db error", "data": []})
        res = []
        if rows:
            for i in rows:
                row = {
                    "id": i.get("id"),
                    "name": i.get("name")
                }
                res.append(row)
        self.write({"error": 0, "errmsg": "ok", "data": res})


class Application(tornado.web.Application):
    def __init__(self):
        urls = [
            (r"/", IndexHandler),
            (r"/query", QueryHandler),
        ]
        settings = dict(
            debug="True",
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            template_path=os.path.join(os.path.dirname(__file__), "template"),
        )
        # 重载父类application
        super(Application, self).__init__(handlers=urls, **settings)
        # 创建一个全局mysql连接实例供handler使用
        self.db = torndb.Connection(
            host="127.0.0.1",
            database="pytest",
            user="root",
            password="root"
        )


if __name__ == '__main__':
    options.parse_command_line()
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
