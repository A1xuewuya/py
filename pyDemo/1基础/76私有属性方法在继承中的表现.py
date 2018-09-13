#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 


class A:
    def __init__(self):
        self.name = "你好"
        self.__age = 20

    def test1(self):
        print("test1...")

    def __test2(self):
        print("test2...")

    def test3(self):
        self.__test2()
        print(self.__age)

class B(A):
    pass

b = B()
b.test1()
b.test3()
print(b.name)


