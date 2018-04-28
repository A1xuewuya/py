#-*- coding:utf-8 -*-

print('-----------begin')

try:
	# 11/0
	# open('fff.txt')
	print(ff)
	print('--------try')
except (FileNotFoundError,NameError):
	print('this is a Error-----1')
except Exception as ret:
	print('this is a Error-----2')
	print(ret)
else:
	print('--------normal')
finally:
	print('----------finally')

print('----------end')