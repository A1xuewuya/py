#-*- coding:utf-8 -*-

class Animal(object):
	def __init__(self):
		pass

	def eat(self):
		print('------eat-----')

	def drink(self):
		print('------drink------')

	def run(self):
		print('------run------')

class Dog(Animal):
	def __init__(self):
		pass

	def dark(self):
		print('-------wawajiao-----')

class Cat(Animal):
	def __init__(self):
		pass

	def miao(self):
		print('----miaomiao--------')

class Xtq(Dog):
	def __init__(self):
		pass

	def xtqdark(self):
		print('----xtqdark-----')

	def dark(self):
		print('------overdark------')
		'''Dog.dark(self)'''
		# super().dark()

	def eat(self):
		print('-----overeat-------')
		'''Animal.eat(self)'''
		# super().eat()

xtq = Xtq()
xtq.xtqdark()
xtq.dark()
xtq.eat()