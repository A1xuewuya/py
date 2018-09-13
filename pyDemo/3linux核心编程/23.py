import time
import threading


# 阻塞和非阻塞 同步和异步

class MyThread1(threading.Thread):
    def __init__(self):
        super(MyThread1, self).__init__()

    def run(self):
        while True:
            if lock1.acquire():
                print("-----Task 1-------")
                time.sleep(1)
                lock2.release()


class MyThread2(threading.Thread):
    def __init__(self):
        super(MyThread2, self).__init__()

    def run(self):
        while True:
            if lock2.acquire():
                print("-----Task 2-------")
                time.sleep(1)
                lock3.release()


class MyThread3(threading.Thread):
    def __init__(self):
        super(MyThread3, self).__init__()

    def run(self):
        while True:
            if lock3.acquire():
                print("-----Task 3-------")
                time.sleep(1)
                lock1.release()


if __name__ == '__main__':
    # 创建线程锁 默认没有锁上
    lock1 = threading.Lock()

    # 创建锁，并且锁上
    lock2 = threading.Lock()
    lock2.acquire()

    # 创建锁，并且锁上
    lock3 = threading.Lock()
    lock3.acquire()

    # 创建线程
    t1 = MyThread1()
    t2 = MyThread2()
    t3 = MyThread3()

    t1.start()
    t2.start()
    t3.start()
