from threading import Thread, Lock

# 线程互斥锁斥修改全局变量

g_num = 0


def work1():
    global g_num
    for i in range(1000000):
        mutex.acquire()  # 这个线程和work2线程都在抢着对对Mutex指向的锁进行上锁，如果有一方成功上锁，则另一方堵塞，知道锁被解开，
        g_num += 1
        mutex.release()  # 对mutex指向的那个锁进行解锁，只要开了锁，接下来会让所有因为这个锁而堵塞的进程，进行抢着上锁
    print("work1----num is %s" % g_num)


def work2():
    global g_num
    for i in range(1000000):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("work2-----num is %s" % g_num)


# 最开始打印主线程num
print("main-----num is %s" % g_num)

# 创建一把互斥锁，默认是没有上锁的
mutex = Lock()

# 创建一个线程
w1 = Thread(target=work1)
w1.start()

# time.sleep(2)  # 暂停两秒让线程w1执行完成

# 创建线程
w2 = Thread(target=work2)
w2.start()
