#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 简单工厂模式


class CarStore(object):
    def __init__(self):
        self.factory = Factory()

    def order(self, car_type):
        return self.factory.select_car_by_type(car_type)


class Factory(object):
    def select_car_by_type(self, car_type):
        if car_type == "索纳塔":
            return Suonata()
        elif car_type == "明途":
            return Mingtu()
        elif car_type == "奥迪":
            return Aodi()


class Car(object):
    def move(self):
        print("车在移动...")

    def music(self):
        print("车放音乐...")


class Suonata(Car):
    pass


class Mingtu(Car):
    pass


class Aodi(Car):
    def aodi(self):
        print("奥迪")


car = CarStore().order("奥迪")
car.move()
car.music()
car.aodi()
