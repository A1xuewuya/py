#!/usr/bin/env python
# -*- coding:utf-8 -*-
# process-class 类实现子进程

import time
from multiprocessing import Process


class PersonClass(Process):
    def __init__(self):
        super(PersonClass, self).__init__()
        # super().__init__()

    def run(self):
        while True:
            print("---子进程执行....")
            time.sleep(2)


if __name__ == '__main__':
    p1 = PersonClass()
    p1.start()
    while True:
        print("-----主进程执行...")
        time.sleep(2)
