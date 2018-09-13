#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 全部变量在多个进程中不共享
import os
import time

a = 100

result = os.fork()
if result > 0:
    print("主进程...")
    a += 1
    print(a)
    time.sleep(2)
else:
    print("子进程...")
    print(a)
