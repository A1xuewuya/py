#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 

def w1(func):
    def inner(a, b):
        func(a, b)

    return inner

@w1
def test(a, b):
    print("a=%d, b=%d" % (a, b))


test(11, 22)
