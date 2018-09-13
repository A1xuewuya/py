#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 

"""
class Test(object):
    def __init__(self):
        self.__age = 20

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


# property封装setter getter
t = Test()
# 通过property赋值
print(t.age)
# 通过property设置值
t.age = 23
print(t.age)
"""


class Test(object):
    def __init__(self):
        self.name = "你好世界"
        self.__age = 22

    def getAge(self):
        return self.__age

    def setAge(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


test = Test()
# print(test.getAge()) 有点麻烦需求调用方法 ，下面对其进行升级
# 获取Test类里面的age属性
print(test.age)
# 设置age私有属性
test.age = 25
print(test.age)