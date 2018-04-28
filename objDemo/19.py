#-*- coding:utf-8 -*-

from keyword import kwlist
from sys import getrefcount

class People(object):
	pass

a = People()
b = a
c = a 
# print(kwlist)
print(getrefcount(a))