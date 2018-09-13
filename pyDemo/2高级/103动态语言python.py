#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
# 动态给实例添加属性


class Person(object):
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age


p = Person("你好", 20)
print(p.name)
print(p.age)

# 给p实例动态添加属性
p.sex = "male"
print(p.sex)

# 给类Person添加一个属性
p1 = Person("世界", 22)
Person.sex = "female"
print(p1.sex)


# 给实例p1动态添加一个实例方法

def run(self):
    print("run....")


import types

p1.run = types.MethodType(run, p1)
p1.run()


# 动态添加静态方法属于类里面的方法
@staticmethod
def print_static():
    print("static..method...")


Person.print_static = print_static
Person.print_static()


# 动态添加类属性
@classmethod
def eat(cls):
    print("eat....类方法")


Person.eat = eat
Person.eat()
