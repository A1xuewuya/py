# -*- coding:utf-8 -*-
#
from BaseHandler import BaseHandler


class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.write("index..get")
