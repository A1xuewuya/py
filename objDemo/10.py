 #-*- coding:utf-8 -*-

'''import sys'''
from sys import getrefcount

class People(object):
	def __init__(self):
		pass

wt = People()
yy = wt
print(getrefcount(wt))