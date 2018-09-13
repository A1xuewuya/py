#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 

def getNums(num):
    """递归函数实现阶乘"""
    if num > 1:
        return num * getNums(num-1)
    else:
        return num


res = getNums(12)
print(res)

