# -*- coding:utf-8 -*-
# 异步运行 把耗时操作放到线程中去运行
import time
import thread


def long_io():
    def fun():
        print("io开始..")
        time.sleep(5)
        print("io结束..")
        return "io result"
    thread.start_new_thread(fun, ())


def req_a():
    print("a开始..")
    res = long_io()
    print(res)
    print("a结束..")


def req_b():
    print("b开始..")
    print("b结束..")


def main():
    req_a()
    req_b()


if __name__ == '__main__':
    main()
