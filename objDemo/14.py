#-*- coding:utf-8 -*-

class Base(object):
	def test(self):
		print('----test-----')

class A(Base):
	def test1(self):
		print('----test1------')

class B(Base):
	def test2(self):
		print('------test2------')

class C(A,B):
	def test3(self):
		print('-------test3-------')

c = C()
c.test3()
c.test2()
c.test1()
c.test()