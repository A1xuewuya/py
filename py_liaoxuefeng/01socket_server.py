#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 导入socket库
import socket
import threading
import time

# 创建socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定监听的地址和端口
s.bind(('0.0.0.0', 9999))

# 调用listen方法监听端口，传入的参数为最大连接数
s.listen(10)
print '开始等待连接...'

def tcplink(sock, addr):
    print 'Accept new connection from %s:%s...' % addr
    sock.send('Welcome 连接到socket_server...')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        sock.send('Hello, %s!' % data)
    sock.close()
    print 'Connection from %s:%s closed.' % addr

# 永久循环来接受客户端的连接
while True:
    # 接受一个新连接
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()


