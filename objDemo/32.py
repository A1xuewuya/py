#-*- coding:utf-8 -*-

class ShortInputException(Exception):
	def __init__(self,length,atleast):
		self.length = length
		self.atleast = atleast



def main():
	try:
		s = input('-----input--:')
		if len(s) <3:
			#
			raise ShortInputException(len(s),3)
	except ShortInputException as res:
		print('error is %s'%res)
		print(res.atleast)
	else:
		print('not have error')

main()