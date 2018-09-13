#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 

"""
class CarStore(object):
    def __init__(self):
        pass

    def order(self, money):
        if money >= 100000:
            return Car()


class Car(object):
    def move(self):
        print("car..move...")

    def run(self):
        print("run...run")


car_store = CarStore()
car = car_store.order(100000)
car.move()
car.run()
"""


class CarStore(object):
    def __init__(self):
        pass

    def order(self, car_type):
        if car_type == "索纳塔":
            return Suonata()
        elif car_type == "明途":
            return Mingtu()


class Car(object):
    def move(self):
        print("car..move...")

    def run(self):
        print("run...run")


class Suonata(Car):
    pass


class Mingtu(Car):
    pass


car_store = CarStore()
car = car_store.order("明途")
car.move()
car.run()
