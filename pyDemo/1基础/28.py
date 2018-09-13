#-*- coding:utf-8 -*-

# Anonymous function
def test(a,b,func):
	result = func(a,b)
	print("%s"%result)

test(11,22,lambda x,y:x+y)