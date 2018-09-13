# -*- coding:utf-8 -*-
import sys

class People:
	pass

xt = People()
yt = xt
print(sys.getrefcount(yt))
print(sys.getrefcount(xt)-1)