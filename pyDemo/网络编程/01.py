import socket

"""
创建套接字socket, 设置ipv4地址,tcp协议
"""
s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

print(s)
