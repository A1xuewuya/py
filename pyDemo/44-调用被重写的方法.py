#-*- coding:utf-8 -*-
class People(object):
	def eat(self):
		print("父类的eat方法")

class A(People):
	def eat(self):
		print("子类的eat方法")
		#
		People.eat(self)
		#
		# super().eat()



a = A()
a.eat()