import time
import threading


# 会出现死锁

class MyThread1(threading.Thread):
    def __init__(self):
        super(MyThread1, self).__init__()

    def run(self):
        if mutex1.acquire():
            print(self.name + '----do1---up----')
            time.sleep(1)

            if mutex2.acquire():
                print(self.name + '----do1---down----')
                mutex2.release()
            mutex1.release()


class MyThread2(threading.Thread):
    def __init__(self):
        super(MyThread2, self).__init__()

    def run(self):
        if mutex2.acquire():
            print(self.name + '----do2---up----')
            time.sleep(1)

            if mutex1.acquire():
                print(self.name + '----do2---down----')
                mutex1.release()
            mutex2.release()


if __name__ == '__main__':
    # 创建两个锁
    mutex1 = threading.Lock()
    mutex2 = threading.Lock()

    t1 = MyThread1()
    t2 = MyThread2()
    t1.start()
    t2.start()
