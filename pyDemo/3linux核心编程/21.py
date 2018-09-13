import time
import threading


# 线程不同，全局变量是公用的，但是局部变量是各自私有的

def test1():
    # 这里的num是局部变量，对于两个不同的线程来说是不同的
    num = 0
    t_name = threading.current_thread().name
    if t_name == "Thread-6":
        num += 1
        print("线程:%s, num is %s" % (t_name, num))
    else:
        time.sleep(2)
        print("线程:%s, num is %s" % (t_name, num))


t1 = threading.Thread(target=test1)
t1.start()

t2 = threading.Thread(target=test1)
t2.start()
