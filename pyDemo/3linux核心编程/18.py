import time
from threading import Thread

# 轮询方式实现互斥修改全局变量

g_num = 0
g_flag = 1


def work1():
    global g_num
    global g_flag
    if g_flag == 1:
        for i in range(1000000):
            g_num += 1
        g_flag = 0
        print("work1----num is %s" % g_num)


def work2():
    global g_num
    global g_flag
    while True:
        if g_flag != 1:
            for i in range(1000000):
                g_num += 1
            break
    print("work2-----num is %s" % g_num)


# 最开始打印主线程num
print("main-----num is %s" % g_num)

w1 = Thread(target=work1)
w1.start()

# time.sleep(2)  # 暂停两秒让线程w1执行完成

w2 = Thread(target=work2)
w2.start()
