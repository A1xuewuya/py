#-*- coding:utf-8 -*-

class People(object):
	def __init__(self,new_name,new_age):
		self.name = new_name
		self.__age = new_age

	def __str__(self):
		pass 

	def get_age(self):
		return self.__age


wt = People('wtcv',22)
print(wt.get_age())