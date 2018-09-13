#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 


class Animal(object):
    # 初始化对象
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "这是动物类"

    def eat(self):
        print("eat...")

    def drink(self):
        print("drink...")

    def intro(self):
        print("name:%s, age:%d" % (self.name, self.age))


# tom = Animal()
# tom.name = "汤姆"
# tom.age = 30
# tom.eat()
# tom.drink()
# tom.intro()
#
#
# lanmao = Animal()
# lanmao.name = "蓝猫"
# lanmao.age = 20
# lanmao.eat()
# lanmao.drink()
# lanmao.intro()


tom = Animal("汤姆", 30)
tom.intro()

lanmao = Animal("蓝猫", 10)
lanmao.intro()


print(tom)
print(lanmao)

