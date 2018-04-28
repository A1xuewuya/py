# -*- coding:utf-8 -*-
# 同步操作
import time


def long_io():
    print("io开始..")
    time.sleep(5)
    print("io结束..")
    return "io result"


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
