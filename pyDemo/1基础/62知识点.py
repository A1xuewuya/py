#!/usr/bin/env python
# -*- coding:utf-8 -*-
# int string tuple为不可变类型  dict list为可变类型
# 可变类型在函数内部可以改变 不可变类型在函数内不会改变


a = 100

def test(num):
    num += num
    return num

res = test(a)
print(res)
print("="*20)