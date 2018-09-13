#!/usr/bin/env python
#

"""
def w1(func):
    print("装饰器w1执行...")

    def inner():
        print("w2正在验证中...")
        func()

    return inner


def w2(func):
    print("装饰器w2执行...")

    def inner():
        print("w2正在验证中...")

    return inner
"""


def test():
    print("test....")


test()
