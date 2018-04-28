# -*- coding:utf-8 -*-
#
import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import options, define

define("port", default=8000, type=int, help="run server on the given port.")

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello itcast.")


class UploadHandler(tornado.web.RequestHandler):
    def post(self):
        files = self.request.files
        img_files = files.get('img')
        if img_files:
            img_file = img_files[0]["body"]
            file = open("./test.jpg", 'w+')
            file.write(img_file)
            file.close()
        self.write("OK")


if __name__ == "__main__":
    options.parse_command_line()
    app = tornado.web.Application([
        (r"/", IndexHandler),
        (r"/upload", UploadHandler),
    ], debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
