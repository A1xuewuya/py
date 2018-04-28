#-*- coding:utf-8 -*-

class People(object):
	def __del__(self):
		print('-------del--------')

a = People()
b = a

del a
del b
print('========')
	