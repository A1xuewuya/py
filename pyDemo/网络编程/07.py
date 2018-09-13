import socket


class SocketManager(object):
    def __init__(self, **kwargs):
        self.userPool = dict()
        self.udp_s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.udp_s.bind((kwargs.get("bind_ip"), kwargs.get("bind_port")))
        while True:
            self.recv_data()

    def recv_data(self):
        recv_tuple = self.udp_s.recvfrom(1024)
        self.send_data(recv_tuple)

    def send_data(self, recv_tuple):
        recv_info, recv_addr = recv_tuple
        # for i in self.userPool:
        self.udp_s.sendto(recv_info, recv_addr)


def main():
    # 配置文件
    config_default = dict(
        bind_ip="",
        bind_port=2345
    )
    SocketManager(**config_default)


if __name__ == '__main__':
    main()
