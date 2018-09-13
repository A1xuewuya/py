# -*- coding:utf-8 -*-

class People(object):
    def __init__(self):
        pass
    def __str__(self):
        pass
    def eat(self):
        print("父类的eat方法")

class Wt(People):
    def __int__(self):
        pass
    def eat(self):
        #调用父类的方法
        People.eat(self)

if __name__ == '__main__':
    wt = Wt()
    wt.eat()