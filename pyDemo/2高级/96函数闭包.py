#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 函数闭包

""" demo
def test(num):
    def test_in(age):
        print(num + age)

    return test_in


ret = test(100)
ret(12)
"""


# 闭包应用

def test(a, b):
    def test_in(x):
        print(a * x + b)

    return test_in


func = test(1, 1)
func(1)

func(2)
