#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 通用装饰器


def w1(func):
    def inner(*args, **kwargs):
        return func(*args, **kwargs)

    return inner


@w1
def test(a, b):
    print("a=%s, b=%s" % (a, b))


test(11, 22)
