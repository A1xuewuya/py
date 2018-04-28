#-*- coding:utf-8 -*-

import time

try:
	try:
		f = open('test.txt')
		while True:
			content = f.readline()
			if len(content) == 0:
				break
			time.sleep(1)
			print(content)
	except Exception:
		pass
	finally:
		f.close()
		print('close this file')

except Exception:
	print('not have this file')