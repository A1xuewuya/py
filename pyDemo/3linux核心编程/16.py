import time
from threading import Thread

num = 0


def work1():
    global num
    num += 1
    print("work1...num is %s" % num)


def work2():
    global num
    num += 1
    print("work2...num is %s" % num)


def main():
    work1()
    work2()


if __name__ == '__main__':
    print("__main__ num is %s" % num)
    t = Thread(target=main)
    t.start()
