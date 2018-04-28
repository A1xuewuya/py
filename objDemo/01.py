#-*- coding:utf-8 -*-

class Cat:
	def eat(self):
		print('eat...')
	def drink(self):
		print('drink...')
	def intr(self):
		print('%s age is %d'%(self.name,self.age))

tom = Cat()
tom.name = 'tom'
tom.age = 12
tom.eat()
tom.drink()
tom.intr()


lanmao = Cat()
lanmao.name = 'lanmao'
lanmao.age = 13
lanmao.eat()
lanmao.drink()
lanmao.intr()