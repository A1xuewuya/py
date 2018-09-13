import os
import time
from multiprocessing import Pool


def test1():
    pass


def test2():
    pass


pool = Pool(3)
pool.apply_async(func=test1(), callback=test2)

time.sleep(5)
