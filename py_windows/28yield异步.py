# -*- coding:utf-8 -*-
#
import time
import thread

gen = None


def long_io():
    global gen
    def func():
        print("开始耗时操作..")
        time.sleep(5)
        print("结束耗时操作..")
        res = "io result"
        try:
            gen.send(res)
        except StopIteration:
            pass
    thread.start_new_thread(func, ())


def req_a():
    print("开始a..")
    res = yield long_io()
    print(res)
    print("离开处理a..")


def req_b():
    print("开始b..")
    time.sleep(2)
    print("结束b..")


def main():
    global gen
    gen = req_a()
    gen.next()
    req_b()
    while 1:
        pass


if __name__ == '__main__':
    main()
