#-*- coding:utf-8 -*-


class People:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __str__(self):
		return 'this is a class'

	def show(self):
		print('hello %s and age %d'%(self.name,self.age))


wt = People('wt', 22)
wt.show()
