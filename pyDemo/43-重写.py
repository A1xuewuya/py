# -*- coding:utf-8 -*-

'''
class People(object):
	def eat(self):
		print("--------eat")

class A(People):
	def eat(self):
		print("-------aaaa--eat")

a = A()
a.eat()
'''

class Animal(object):
	def __init__(self):
		self.name = 'aaa'

	def eat(self):
		print("父类的eat方法")

class Dog(Animal):
	def __init__(self):
		self.name = 'bbb'
	def eat(self):
		print('子类的eat方法')

a = Dog()
a.eat()