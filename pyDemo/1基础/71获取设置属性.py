#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 


class Dog:
    def __init__(self):
        self.age = 0

    def set_age(self, age):
        if age >= 0 & age < 100:
            self.age = age

    def get_age(self):
        return self.age


dog = Dog()
dog.set_age(10)
age = dog.get_age()
print(age)
