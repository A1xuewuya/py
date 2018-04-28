class Animal(object):
	def eat(self):
		print("--------eat")
	def drink(self):
		print("--------drink")

class Dog(Animal):
	def dark(self):
		print("------dark")

a = Dog()
a.dark()
a.drink()