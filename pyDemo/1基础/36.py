#-*- coding:utf-8 -*-

class People:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return "这是people类"
    def sayHello(self):
        print('hello %s'%self.name)

if __name__ == '__main__':
	wt = People('wt',22)
	print(wt)
	print(type(wt))
	wt.sayHello()
