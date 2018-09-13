#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 类名.__mro__ 在调用这个方法时候，搜索的顺序，在某个类中找到方法就停止搜索
#


class Base(object):
    def test(self):
        print("base")

class A(Base):
    def test(self):
        print("A")

class B(Base):
    def test(self):
        print("B")

class C(B, A):
    def test(self):
        print("C")

print(C.__mro__)
c = C()
c.test()