#!/usr/bin/env python
# -*- coding:utf-8 -*-


import tornado.web
import config


if __name__ == '__main__':
    app = tornado.web.Application([], **config.settings)
    print(config.settings)

