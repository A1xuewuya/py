#-*- coding:utf-8 -*-

class Dog(object):
	def __init__(self):
		print('------init')

	def __str__(self):
		print('--------str')

	def __del__(self):
		print('--------del')

	def __new__(cls):
		print('--------new')
		return object.__new__(cls)
		# return super().__new__(cls)

print('-------begin')
xtq = Dog()
del xtq
print('-------end')