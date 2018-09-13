#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 进程执行顺序
import os
import time

# 说不定父进程和子进程谁先执行完
result = os.fork()
if result > 0:
    print("主进程,进程id为:%d" % os.getppid())
    time.sleep(2)
else:
    print("子进程，进程id为:%d " % os.getppid())

