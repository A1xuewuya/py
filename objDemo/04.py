#-*- coding:utf-8 -*-

class Home(object):
	def __init__(self,new_area,new_info,new_addr):
		self.new_area = new_area
		self.new_info = new_info
		self.new_addr = new_addr
		self.left_area = new_area
	def __str__(self):
		return 'left_area is %s'%self.left_area
	def add(self,item):
		self.left_area -=item.get_area()


class Bed(object):
	def __init__(self,new_name,new_area):
		self.name = new_name
		self.area = new_area
	def __str__(self):
		return 'hello bed'
	def get_name(self):
		return self.name
	def get_area(self):
		return self.area

#home object
fangzi = Home(135,'3shi 2ting','Beijing')
#bed object
bed = Bed('hhgz',6)
fangzi.add(bed)
print(fangzi)


