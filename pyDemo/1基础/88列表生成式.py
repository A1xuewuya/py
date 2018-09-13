#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 列表生成式


a = [i for i in range(0, 20)]
b = [i for i in range(10) if i % 2 == 0]
c = [(i, j) for i in range(3) for j in range(2)]

print(a)
print(b)
print(c)
