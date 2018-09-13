#-*- coding:utf-8 -*-

class People:
	def __init__(self):
		pass

	def __str__(self):
		return "这是People类"

	def set_age(self,new_age):
		if new_age>=0 and new_age<=150:
			self.age = new_age
		else:
			self.age = 0

	
	def get_age(self):
		return self.age	

if __name__ == '__main__':
	nzc = People()
	nzc.set_age(22)
	print(nzc.get_age())
	print(nzc)
