#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 调用方只管调用，不管细节

class Dog(object):
    def __init__(self):
        pass

    def print_self(self):
        print("dog...")


class Xiaotq(Dog):
    def print_self(self):
        print("xiaotq...")


def introduce(temp):
    temp.print_self()


dog = Dog()
xiaotq = Xiaotq()
introduce(dog)
introduce(xiaotq)