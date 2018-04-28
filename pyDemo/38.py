class People:
	def __init__(self):
		pass

	def __str__(self):
		pass

#provate function
	def __send_msg(self):
		print("__send_msg----")

#public function
	def send_msg(self,sum):
		if sum >= 10000:
			self.__send_msg()
		else:
			print("not have money")

if __name__ == '__main__':
	nzc = People()
	nzc.send_msg(2)