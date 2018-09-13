#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 


class SweetPotato(object):
    def __init__(self):
        self.cookedString = "生的"
        self.cookedLevel = 0

    def __str__(self):
        return "%s, %d" % (self.cookedString, self.cookedLevel)

    def cook(self, cookedTime):
        self.cookedLevel += cookedTime
        if self.cookedLevel >= 0 and self.cookedLevel < 3:
            self.cookedString = "生的"
        elif self.cookedLevel >= 3 and self.cookedLevel < 5:
            self.cookedString = "稍微熟了"
        elif self.cookedLevel >= 5 and self.cookedLevel < 7:
            self.cookedString = "半生不熟"
        elif self.cookedLevel >= 7 and self.cookedLevel < 10:
            self.cookedString = "熟了"
        elif self.cookedLevel >= 10:
            self.cookedString = "糊了"


# 每一个都会实例化对象
# SweetPotato().cook(1)
# SweetPotato().cook(1)
# SweetPotato().cook(1)
# SweetPotato().cook(1)
# SweetPotato().cook(1)

# 实例化一个对象
digua = SweetPotato()
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(3)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)

