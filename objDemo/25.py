#-*- coding:utf-8 -*-

class Dog(object):
	__instance = None
	__init_flag = False
	def __new__(cls,name):
		if cls.__instance == None:
			cls.__instance = object.__new__(cls)
		return cls.__instance

	def __init__(self,name):
		if Dog.__init_flag == False:
			self.name = name
			Dog.__init_flag = True

a = Dog('aaa')
print(id(a))
print(a.name)

b = Dog('bbbfdf')
print(id(b))
print(b.name)

