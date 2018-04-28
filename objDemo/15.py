#-*- coding:utf-8 -*-


class Base(object):
	def __init__(self):
		pass

	def test(self):
		print('-----Base------')

class A(Base):
	def test(self):
		print('-----A-----')

class B(Base):
	def test(self):
		print('-----B-----')

class C(A,B):
	def test(self):
		print('-----C-----')
		# super().test()
		B.test(self)
		Base.test(self)

c = C()
c.test()
print(C.__mro__)