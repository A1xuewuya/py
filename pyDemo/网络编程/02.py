# -*- coding:utf-8 -*-


import socket

# 发送socket udp协议到指定主机 使用udp发送的数据，每一次都需要写上ip和端口
# 1.  创建套接字 udp协议
s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# 2. 准备接收方的地址
s_addr = ("10.10.136.94", 8080)
# s_addr = ("10.10.121.121", 8000)

# 3. 发送给接收方的消息
# s_con = input("请输入要发送的数据:")
s_con = "world"

# 4. 发送数据
s.sendto(s_con, s_addr)

# 5. 关闭socket
s.close()
