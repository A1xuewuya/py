#-*- coding:utf-8 -*-

class People(object):
	def __init__(self):
		pass

	def set_info(self,temp_name,temp_age):
		self.name = temp_name
		if temp_age>=0 and temp_age<=100:
			self.age = temp_age
		else:
			self.age = 0
			
	def get_info(self):
		print('name is %s,age is %d'%(self.name,self.age))

wt = People()
wt.set_info('wtex',18)
wt.get_info()