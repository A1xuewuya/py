#!/usr/bin/env python
# -*- coding:utf-8 -*-
#


class Animal(object):
    def __init__(self):
        print("animal....__init__")
        # self.name = "animal"

    def eat(self):
        print("eat....")


class Dog(Animal):
    def __init__(self):
        # self.name = "tom"
        # Animal().__init__()
        print("dog...__init__")

    def dark(self):
        print("dark....")


tom = Dog()
tom.dark()
tom.eat()
