import socket

# TCP 客户端
c_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# 连接服务器
s_addr = ("10.10.136.94", 8000)
c_socket.connect(s_addr)

# 发送数据
c_send_str = input("请输入要发送的数据:")
c_socket.send(c_send_str.encode("gb2312"))

# 接受数据
recv_data = c_socket.recv(1024).decode("gb2312")

# 打印数据
print("%s" % recv_data)

# 关闭套接字
# c_socket.close()
