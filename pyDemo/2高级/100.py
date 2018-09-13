#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 两个装饰器的效果


def w1(func):
    print("装饰器w1执行...")

    def inner():
        print("w1正在验证中...")
        func()

    return inner


def w2(func):
    print("装饰器w2执行...")

    def inner():
        print("w2正在验证中...")
        func()

    return inner


@w1
@w2
def test():
    print("你好世界")


test()

