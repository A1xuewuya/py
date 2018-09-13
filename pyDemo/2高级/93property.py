#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 


class Test(object):
    def __init__(self):
        self.__age = 20

    def getAge(self):
        return self.__age

    def setAge(self, age):
        self.__age = age

    p_age = property(getAge, setAge)


# 第一种调用方法
# t = Test()
# age = t.getAge()
# t.setAge(22)

# property封装setter getter
t = Test()
# 通过property赋值
print(t.p_age)
# 通过property设置值
t.p_age = 23



