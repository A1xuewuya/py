# -*- coding:utf-8 -*-
#
import tornado.httpserver
import tornado.ioloop
from tornado.options import options, define
from application import Application

define("port", default="8000", type=int, help="server port..")


def main():
    options.parse_command_line()
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
