import socket

# python3中发送数据

# 接收发送数据并且处理
udp_ip = input("请输入要发送的ip:")
udp_port = input("请输入要发送的端口:")
udp_data = input("请输入要发送的内容:")
udp_data = udp_data.encode("gb2312")
udp_cell = (udp_ip, int(udp_port))

# 创建socket
udp_s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# 发送数据
# udp_s.sendto(udp_data.encode("utf-8"), udp_cell)
udp_s.sendto(udp_data, udp_cell)

# 关闭socket
udp_s.close()
