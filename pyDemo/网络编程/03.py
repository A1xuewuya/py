import socket

# 1.  创建套接字 udp协议
udp_s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# 2. 接收方绑定端口 ip地址和端口号，一般不写，表示本机的任意一个ip
udp_bind_addr = ("", 8000)
udp_s.bind(udp_bind_addr)

# 3. 等待接受对方的数据
recv_data = udp_s.recvfrom(1024)

# 4. 显示接收到的数据
print(recv_data)

# 5. 关闭套接字
udp_s.close()
