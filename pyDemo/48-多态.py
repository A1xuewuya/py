class Dog(object):
	def __init__(self):
		pass
	def print_self(self):
		print("-----dog")

class Xtq(Dog):
	def __init__(self):
		pass
	def print_self(self):
		print("-----xtq")

def introduce(temp):
	temp.print_self()

dog1 = Dog()
dog2 = Xtq()

introduce(dog1)
introduce(dog2)

