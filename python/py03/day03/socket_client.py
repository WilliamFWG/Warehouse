import socket


if __name__ == '__main__':
    # TCP客户端
    """
    1.创建套接字
    2.IP及端口链接TCP服务器
    3.收发数据
    4.关闭
    """
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 链接服务器
    server_ip = "127.0.0.1"
    server_port = int("8001")
    tcp_client.connect((server_ip, server_port))  # 元祖

    # 发送数据
    send_data = input('请输入要发送的数据')
    tcp_client.send(send_data.encode())

    # 接收数据
    rec_data = tcp_client.recv(1024)
    print(rec_data.decode())

    # 关闭
    tcp_client.close()