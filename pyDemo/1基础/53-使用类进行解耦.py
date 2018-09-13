class CarStore(object):
	def __init__(self):
		self.factory = Factory()
	def __str__(self):
		pass
	def __del__(self):
		pass
	def order(self,car_type):
		return self.factory.select_car_by_type(car_type)

class Factory(object):
	def select_car_by_type(car_type):
		if car_type == "baoma":
			return Baoma()
		elif car_type == "aodi":
			return Aodi()
		else:
			pass	

class Car(object):
	def __init__(self):
		pass
	def __str__(self):
		pass
	def __del__(self):
		pass

	def move(self):
		print("-------move")
	def run(self):
		print("-------run")

class Baoma(Car):
	def __init__(self):
		print("=======baoma")
	def __str__(self):
		return "++++++baoma"

class Aodi(Car):
	def __init__(self):
		print("=======aodi")
	def __str__(self):
		return "+++++++aodi"


car_store = CarStore()
car = car_store.order("aodi")
car.move()
car.run()
print(car)
print(car)

