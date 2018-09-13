import socket


def main():
    udp_s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    udp_bind_addr = ("", 8001)
    udp_s.bind(udp_bind_addr)

    while True:
        recv_tuple = udp_s.recvfrom(1024)
        recv_data, recv_addr = recv_tuple
        recv_data = recv_data.decode("gb2312")
        print("接受到数据为:%s" % recv_data)
        udp_s.sendto("你好啊，这是返回的消息".encode("gb2312"), recv_addr)


if __name__ == '__main__':
    main()
