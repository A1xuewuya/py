#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 

# 模块重新导入
# 模块循环导入
# == is

"""
a = [11, 22, 33]
b = [11, 22, 33]
c = a

print(id(a))
print(id(b))
print(id(c))
"""

# 深拷贝、浅拷贝
import copy

a = [11, 22, 33]
b = [11, 22, 33]
c = copy.deepcopy(a)
print(id(a))
print(id(b))
print(id(c))

