#-*- coding:utf-8 -*-

class Game(object):
	#
	num = 0

	def __init__(self):
		self.name = 'laowang'

	@classmethod
	def add_num(cls):
		cls.num = 101

	@staticmethod
	def show():
		print('------begin--------')
		print('-------hello-------')

# Game.add_num()
game = Game()
# game.add_num()
# print(Game.num)
# Game.show()
game.show()