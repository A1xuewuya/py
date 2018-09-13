#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 


class People(object):
    def __init__(self):
        print("people....__init__")

    def run(self):
        print("people___run___")


class Wt(People):
    def run(self):
        print("wt...run...")
        # 第一种调用父类的方法
        People.run(self)
        # 第二种调用父类的方法
        super().run()


wt = Wt()
wt.run()
