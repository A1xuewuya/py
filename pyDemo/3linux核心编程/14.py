import time
import threading

"""
使用线程Thread完成多任务
"""


def test():
    print("线程执行....")
    time.sleep(1)


for i in range(5):
    t = threading.Thread(target=test)
    t.start()
