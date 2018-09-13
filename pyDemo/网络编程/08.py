import socket

# TCP编程 服务端
s_server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# 绑定端口
tcp_addr = ("", 8000)
s_server.bind(tcp_addr)

# 把主动socket变为被动socket模式
s_server.listen(6)

# 接受tcp连接返回socket
c_socket, c_info = s_server.accept()

# 返回接收到的数据
recv_data = c_socket.recv(1024)

# 打印数据
print("%s ; %s" % (recv_data, str(c_info)))

# 关闭socket
s_server.close()
c_socket.close()
