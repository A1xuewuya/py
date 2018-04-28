#-*- coding:utf-8 -*-

class SweetPrtato(object):
	def __init__(self):
		self.cookedLeavel = 0
		self.cookedString = 'shengde'
		self.seasoning = []

	def __str__(self):
		return '%s(%d) %s'%(self.cookedString,self.cookedLeavel,
			str(self.seasoning))

	def cook(self,cookedTime):
		self.cookedLeavel += cookedTime
		if self.cookedLeavel>=0 and self.cookedLeavel<3:
			self.cookedString = 'shengde'
		elif self.cookedLeavel>=3 and self.cookedLeavel<8:
			self.cookedString = 'bansheng'
		elif self.cookedLeavel>=8 and self.cookedLeavel<10:
			self.cookedString = 'shoule'
		else:
			self.cookedString = 'hule'

	def add(self,seasoning):
		self.seasoning.append(seasoning)


di_gua = SweetPrtato()
di_gua.cook(1)
di_gua.cook(1)
di_gua.cook(1)
di_gua.cook(1)
di_gua.cook(1)
di_gua.cook(1)
di_gua.cook(1)
di_gua.cook(1)
di_gua.cook(1)
di_gua.add('你好')
di_gua.add('rrrr')
print(di_gua)
