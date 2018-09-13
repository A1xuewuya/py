#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 


# 闭包完成装饰器
def W1(func):
    def inner():
        print("inner...验证")
        func()

    return inner


# f1 = W1(f1)
@W1
def f1():
    print("f1....")


@W1
def f2():
    print("f2....")


# f1 = W1(f1)
f1()
f2()
