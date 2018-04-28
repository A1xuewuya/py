#-*- coding:utf-8 -*-

class Info(object):
	def __init__(self):
		pass

	def __send_msg(self):
		print('send the msg...')
	
	def send(self,temp_money):
		if temp_money>=100:
			self.__send_msg()
		else:
			print('not have money')

wt = Info()
wt.send(101)