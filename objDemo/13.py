#-*- coding:utf-8 -*-

class A:
	def __init__(self):
		self.name = 'wt'
		self.__age = 20

	def __test1(self):
		print('-----test1-------')

	def test2(self):
		print('-----test2------')

	def test3(self):
		print(self.__age)
		self.__test1()

class B(A):
	pass

b = B()
b.test2()
b.test3()
