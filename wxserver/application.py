# -*- coding:utf-8 -*-
#
import os
import tornado.web
from urls import urls
from configs import config_default

# application参数
config_default.settings["static_path"] = os.path.join(os.path.dirname(__file__), "static")
config_default.settings["template_path"] = os.path.join(os.path.dirname(__file__), "template")


class Application(tornado.web.Application):
    def __init__(self):
        super(Application, self).__init__(handlers=urls, **config_default.settings)

