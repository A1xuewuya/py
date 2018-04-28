class Tool(object):

	num = 22

	def __init__(self,new_name):
		self.name = new_name
		print(self.name)
	def __str__(self):
		return "-----str----"
	def __del__(self):
		pass

a = Tool("------a")
b = Tool("------b")
c = Tool("------c")
print(c.num)