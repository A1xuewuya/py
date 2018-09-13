#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __slots__变量，来限制该class实例能添加的属性


class Person(object):
    __slots__ = ("name", "age")

    def __init__(self):
        pass


try:
    p = Person()
    p.name = "你好"
    p.age = 22
    p.addr = "北京"
except Exception as e:
    print(e)
