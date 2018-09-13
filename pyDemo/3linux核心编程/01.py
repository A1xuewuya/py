import os
import time

# 这种写法运行在linux平台上
# # os.fork()创建子进程，返回值有两个：其中父进程大于0，子进程为0
# result = os.fork()
# if result == 0:
#     while True:
#         print("这是子进程执行....")
#         time.sleep(2)
# else:
#     while True:
#         print("这是父进程执行....")
#         time.sleep(2)

pid = os.fork()
if pid < 0:
    print("fork调用失败...")
elif pid == 0:
    print("子进程:%d, 父进程是:%d" % (os.getpid(), os.getppid()))
else:
    print("父进程:%d, 子进程是:%d" % (os.getpid(), pid))
print("父进程和子进程都执行的代码...")
