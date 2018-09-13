import time
from threading import Thread

# 修改进程中线程全局变量

num = 0


def work1():
    global num
    for i in range(1000000):
        num += 1
    print("work1----num is %s" % num)


def work2():
    global num
    for i in range(1000000):
        num += 1
    print("work2-----num is %s" % num)


# 最开始打印主线程num
print("main-----num is %s" % num)

w1 = Thread(target=work1)
w1.start()

time.sleep(2)  # 暂停两秒让线程w1执行完成

w2 = Thread(target=work2)
w2.start()
