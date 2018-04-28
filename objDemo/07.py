#-*- coding:utf-8 -*- 

class People(object):
	def __init__(self,new_name,new_age,new_sex):
		self.__name = new_name
		self.age = new_age
		self.sex = new_sex

	def __str__(self):
		return 'name is %s,age is %d,sex is %s'%(self.name,self.age,self.sex)

	def __get_money(self,new_money):
		self.money = new_money+2000

	def count(self,new_money):
		self.__get_money(new_money)

	def show_money(self):
		print(self.money) 

	def get_name(self):
		print(self.__name)

wt = People('wt123',20,'nan')
wt.count(1000)
wt.show_money()
wt.get_name()


