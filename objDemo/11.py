#-*- coding:utf-8 -*-

class Animal(object):
	def __init__(self):
		pass

	def eat(self):
		print('--------eat')

	def drink(self):
		print('-------drink')

	def run(self):
		print('-------run')

class Dog(Animal):
	def __init__(self):
		pass

	def dark(self):
		print('-------dark')

class Cat(Animal):
	def __init__(self):
		pass

	def catch(self):
		print('-------catch')

taidi = Dog()
taidi.eat()
taidi.dark()

baomao = Cat()
baomao.run()
baomao.catch()