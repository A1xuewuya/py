import socket

# 创建socket
udp_s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# 绑定端口
udp_bind_addr = ("", 8000)
udp_s.bind(udp_bind_addr)

# 等待接受客户端的数据
while True:
    recv_tuple = udp_s.recvfrom(1024)
    recv_data, recv_info = recv_tuple
    print("客户端发送的数据是: %s " % recv_data.decode("gb2312"))
    print("客户端信息: %s" % str(recv_info))


# udp_s.close()


