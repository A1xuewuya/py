#-*- coding:utf-8 -*-

class Base(object):
	def __init__(self):
		pass

	def print_self(self):
		print('------base-------')

class A(Base):
	def __init__(self):
		pass

	def print_self(self):
		print('-------A-------')

def introduce(temp):
	temp.print_self()


base = Base()
a = A()
introduce(base)
introduce(a)