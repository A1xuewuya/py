#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 魔术方法__new__方法


class Person(object):
    def __str__(self):
        print("__str__")

    def __init__(self):
        print("__init__")

    def __new__(cls, *args, **kwargs):
        # print("__new__") 实例化对象方法 ，这里重写父类的实例化方法生成对象引用传递到__init__
        return object.__new__(cls)

    def __del__(self):
        print("__del__")


xwy = Person()
