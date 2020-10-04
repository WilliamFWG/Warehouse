import socket

if __name__ == '__main__':
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = ('127.0.0.1', 8001)
    tcp_server.bind(address)
    tcp_server.listen(5)
    client_socket, client_addr = tcp_server.accept()
    #print(tcp_server.accept())
    recv_data = client_socket.recv(1024)
    print(recv_data.decode())
    print(client_addr)
    client_socket.send("Thank you".encode())
    client_socket.close()
