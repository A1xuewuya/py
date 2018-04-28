# -*- coding:utf-8 -*-
#
import json
import hashlib
import xmltodict
import tornado.web
from configs.config_default import WECHAT_TOKEN


class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        print("setting headers...")
        self.set_header("Server", "nzc")

    def initialize(self):
        pass

    def prepare(self):
        if self.request.headers.get("Content-Type", "").startswith("application/json"):
            self.receive_data = json.loads(self.request.body)
        elif self.request.headers.get("Content-Type", "").startswith("text/xml"):
            self.receive_data = xmltodict.parse(self.request.body)
            self.receive_data = self.receive_data["xml"]
        elif self.request.headers.get("Content-Type", "").startswith("application/xml"):
            self.receive_data = xmltodict.parse(self.request.body)
            self.receive_data = self.receive_data["xml"]
        elif self.request.headers.get("Content-Type", "").startswith("text/xml"):
            self.receive_data = xmltodict.parse(self.request.body)
            self.receive_data = self.receive_data["xml"]
        else:
            self.receive_data = None
