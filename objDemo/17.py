#-*- coding:utf-8 -*-

class Base(object):

	#lei shuxing
	num = 0

	def __init__(self,new_name):
		self.name = new_name
		Base.num += 1

a = Base('aaa')
b = Base('bbb')
c = Base('ccc')
print(Base.num)
