import threading
import time


class MyThread(threading.Thread):
    def __init__(self):
        super(MyThread, self).__init__()

    def run(self):
        for i in range(3):
            print("I am %s ,%s" % (self.name, i))
            time.sleep(1)


for i in range(3):
    t = MyThread()
    t.start()
