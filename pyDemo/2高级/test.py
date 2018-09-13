#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
# 一个模块中如果对象能够被使用，则放到__all__列表中
__all__ = ["test1", "test2"]


def test1():
    print("...test1...")


def test2():
    print("...test2...")


if __name__ == '__main__':
    test1()
