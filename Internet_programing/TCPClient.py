# 创建socket对象
import socket

socket_tcp_client = socket.socket()

# 确定目标ip和端口号
ip_port = ('10.31.153.41', 10081)
socket_tcp_client.connect(ip_port)
# 发送消息
while True:
    data = input("请输入要发送的消息:\n")
    if data == '':
        continue

    if data == 'exit':
        break

    socket_tcp_client.sendall(bytes(data, encoding='utf-8'))
    receive = socket_tcp_client.recv(1024)
    print(str(receive,encoding='utf-8'))

# 关闭连接
socket_tcp_client.close()
