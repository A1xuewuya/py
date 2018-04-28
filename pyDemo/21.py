#-*- coding:utf-8 -*-

a = 100
def test1():
	# global a
	a = 222

def test2():
	print("%d"%a)

test1()
test2()