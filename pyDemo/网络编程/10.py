import socket

# 单进程服务器
# 创建服务器套接字
s_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# 重复使用绑定的信息
s_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

loacl_addr = ('', 2345)

s_socket.bind(loacl_addr)

s_socket.listen(5)

while True:
    print("------------主进程，等待客户端连接")

    c_socket, dest_addr = s_socket.accept()

    print("-----------主进程，接下来负责处理数据[%s] " % str(dest_addr))

    try:
        while True:
            recv_data = c_socket.recv(1024)
            if len(recv_data) > 0:
                print("recv[%s]:%s" % (str(dest_addr), recv_data))
            else:
                print("[%s]客户端已关闭" % str(dest_addr))
                break
    finally:
        c_socket.close()


