import os

result = os.fork()
if result > 0:
    print("这是父进程，进程id为:%d" % os.getpid())
else:
    print("这是子进程，进程id为:%d，其父进程id为:%d" % (os.getpid(), os.getppid()))
