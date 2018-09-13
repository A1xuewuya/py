#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
# 写入多行文件
# f = open("test.txt", "w")
# i = 0
# while i < 10:
#     f.write("你好世界，这是 %s \n" % i)
#     i += 1
#
# f.close()

f = open("test.txt", "r")
con = f.readlines()
data = []
for v in con:
    data.append(v.strip())

f.close()
