#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
try:
    open("xxx.txt")
    # print(num)
    print("你好")

except NameError as e:
    print(e)
except FileNotFoundError as e:
    print(e)
except Exception:
    pass