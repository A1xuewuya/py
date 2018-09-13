#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 

def w1(func):
    def inner(a, b, *args):
        test = args
        func(a, b, *args)

    return inner

@w1
def test(a, b, *args):
    print("a=%d, b=%d" % (a, b))


test(11, 22, 33)
