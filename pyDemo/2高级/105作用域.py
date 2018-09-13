#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
# 全局变量 ==> 全局作用域
a = 100
b = 200

res = globals()
print(res['a'])
# 改变全局变量res，查看原先globals()是否改变
res['a'] = 300
print(globals()['a'])


def test():
    name = "你好"
    age = 22
    print("这是局部作用域:%s" % locals())


test()
