#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 


class Tool(object):
    # 类属性
    num = 0

    def __init__(self, name):
        # 实例属性
        self.name = name
        # 对类属性操作
        Tool.num += 1

tool1 = Tool("铁锹")
tool2 = Tool("军铁锹")
print(Tool.num)
pass
