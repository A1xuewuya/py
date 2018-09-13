#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 


class Tool(object):
    # 类属性
    num = 0

    # 实例方法
    def __init__(self, name):
        # 实例属性
        self.name = name

    @classmethod
    def add_num(cls):
        cls.num += 1

    @staticmethod
    def print_menu():
        print("静态方法")


# 通过实例操作类方法
tool = Tool("你好")
tool.add_num()

# 直接调用类方法
Tool.add_num()

# 调用静态方法
Tool.print_menu()
tool.print_menu()
