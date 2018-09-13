#!/usr/bin/env python
# -*- coding:utf-8 -*-
#

# class Dog(object):
#     def __init__(self):
#         self.name = "小狗"
#         self.__age = 20
#
# dog = Dog()
# dog.__age


class Send(object):
    def __init__(self):
        pass

    def __send_msg(self):
        print("短息已经发送...")

    def send_msg(self, money):
        if money >= 10:
            self.__send_msg()
        else:
            print("余额不足，请充值后发送...")



xwy = Send()
xwy.send_msg()