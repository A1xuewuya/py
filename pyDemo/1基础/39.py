class People:
	def __del__(self):
		print("--------over---------")


xxx = People()
yyy = xxx
del xxx
del yyy
print("=========")