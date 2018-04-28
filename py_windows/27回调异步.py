# -*- coding:utf-8 -*-
#
import time
import thread


def long_io(cb):
    def func(callback):
        print("开始耗时操作..")
        time.sleep(3)
        print("结束耗时操作..")
        res = "io result"
        callback(res)
    thread.start_new_thread(func, (cb,))


def on_finish(res):
    print("开始执行回调函数..")
    print(res)
    print("结束执行回调函数..")


def req_a():
    print("开始a..")
    res = long_io(on_finish)
    print("离开处理a..")


def req_b():
    print("开始b..")
    print("结束b..")


def main():
    req_a()
    req_b()
    while 1:
        pass


if __name__ == '__main__':
    main()
