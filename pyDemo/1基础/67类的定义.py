#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 

class Dog:

    def eat(self):
        print("eat...")

    def drink(self):
        print("drink...")

# 正常调用
dog = Dog()
dog.eat()
dog.name = "小白"
dog.age = 5

print("小狗的名字是：%s，小狗的年龄是：%d" % (dog.name, dog.age))

# 链式调用
# Dog().eat()
