class People:
	def __init__(self,name,age):
		self.name = name
		self.age = age
		print("__init__")

	def __str__(self):
		return "this is str "
		
	def say(self):
		print("%s age is %d"%(self.name,self.age))


if __name__ == '__main__':
	nzc = People("nzc",22)
	print(nzc)
