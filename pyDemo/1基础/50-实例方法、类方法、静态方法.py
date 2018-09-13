class Game(object):
	name = "cf"

	def __init__(self):
		pass
		#self.name="dnf"
	def __str__(self):
		pass
	def __del__(self):
		pass

	
	@classmethod
	def say_name(cls):
		cls.name = 'xxxx'
		print(cls.name)

	@staticmethod
	def print_name():
		print("-------")
		print("--------z")
		print("---------ff")
	
a = Game()
a.say_name()
#
Game.say_name()
#
Game.print_name()
#
a.print_name()
