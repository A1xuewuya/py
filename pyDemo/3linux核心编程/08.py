#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
import time
from multiprocessing import Process


def run_proc():
    while True:
        print("子进程执行....")
        time.sleep(2)


if __name__ == '__main__':
    p = Process(target=run_proc)
    p.start()
    p.join()  # 堵塞，等子进程执行完毕之后才能执行
    print("主进程执行完毕...")
