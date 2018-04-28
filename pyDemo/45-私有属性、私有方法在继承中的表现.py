class Animal(object):
	def __init__(self):
		self.name = "ani"
		self.__age = 5

	def __test1(self):
		print("-----test1")

	def test2(self):
		print("-----test2")

	def test3(self):
		self.__test1()
		print(self.__age)

class Dog(Animal):
	pass

dog = Dog()
dog.test2()
# dog.__test1()
dog.test3()
