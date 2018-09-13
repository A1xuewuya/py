class Animal:
	
	def _init__(self):
		pass
	def __str__(self):
		pass
	def __del__(self):
		pass

	def eat(self):
		print("-------eat-------")
	def drink(self):
		print("-------drink-------")
	def sleep(self):
		print("-------sleep-------")
	def run(self):
		print("-------run-------")

class Dog(Animal):
	def dark(self):
		print("-------dark-------")

class Cat(Animal):
	def miao(self):
		print("-------miao-------")

c = Cat()
c.miao()
c.eat()
c.run()
