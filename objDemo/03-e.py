#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Sweetprotato:
    def __init__(self):
        self.cookTime = 0
        self.cookString = '生的'
        self.cookLevel = 0
        self.cookOther = []

    def __str__(self):
        return '当前烹饪时间是：%s，烹饪度是：%s, 佐料是：%s' % (self.cookTime, self.cookLevel, str(self.cookOther))

    def cook(self, time):
        self.cookLevel += time
        if self.cookLevel > 0 and self.cookLevel <= 3:
            self.cookString = '3分熟'
        elif self.cookLevel >3 and self.cookLevel <= 7:
            self.cookString = '7分熟'
        elif self.cookLevel > 7 and self.cookLevel <= 10:
            self.cookString = '快熟了'
        elif self.cookLevel > 10:
            self.cookString = '烧糊了'

    def add(self, other):
        self.cookOther.append(other)

# 创建对象
digua = Sweetprotato()
digua.cook(1)
digua.cook(1)
digua.cook(1)
digua.cook(1)
digua.cook(1)
digua.cook(1)
digua.cook(1)
digua.add('番茄酱')
digua.add('硕果')
print(digua)
