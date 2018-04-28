#-*- coding:utf-8 -*-

def test1():
	print('-------1-1')
	print(num)
	print('-------1-2')

def test2():
	print('-------2-1')
	test1()
	print('-------2-2')

def test3():
	try:
		print('-----3-1')
		test2()
		print('-----3-2')
	except Exception as res:
		print(res)

test3()
print('==============')
# test2()