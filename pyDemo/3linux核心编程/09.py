import time
from multiprocessing import Process


def run_proc():
    while True:
        # print("子进程执行...")
        p = Process(target=run_proc)
        p.start()


if __name__ == '__main__':
    p = Process(target=run_proc)
    p.start()
    p.join()
    # print("主进程执行...")
