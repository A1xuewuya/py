#-*- coding:utf-8 -*-

class CarStore(object):
	def __init__(self):
		self.factory = Factory()

	def order(self,carType):
		return self.factory.selectCarType(carType)

class Factory(object):
	def __init__(self):
		pass

	def selectCarType(self,carType):
		if carType=='bc':
			return Bc()
		elif carType=='bmw':
			return Bmw()
		elif carType=='aodi':
			return Aodi()

class Car(object):
	def drive(self):
		print('-------drive---')

	def music(self):
		print('------music---')

	def stop(self):
		print('------stop---')

class Bc(Car):
	pass

class Bmw(Car):
	pass

class Aodi(Car):
	pass

car_store = CarStore()
car = car_store.order('aodi')
car.music()
