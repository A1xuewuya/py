#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 生成器完成多任务-----协程方法


def test1():
    while True:
        print("-------1")
        yield None


def test2():
    while True:
        print("--------2")
        yield None


# 生成两个生成器
t1 = test1()
t2 = test2()
while True:
    t1.__next__()
    t2.__next__()
