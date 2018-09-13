#!/usr/bin/env python
# -*- coding:utf-8 -*-
# process创建子进程

import os
import time
from multiprocessing import Process


def test_jincheng(name):
    while True:
        print("子进程执行中...")
        time.sleep(1)


if __name__ == '__main__':
    p = Process(target=test_jincheng, args=('test',))
    p.start()
    p.join()

    while True:
        time.sleep(2)
        print("主进程执行....")
