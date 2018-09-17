import socket

#创建socket对象
socket_tcp_server = socket.socket()
#绑定ip和端口
ip_port = ('10.31.153.41',10081)
socket_tcp_server.bind(ip_port)
flag = 0
while True:
    if flag is 0:
        # listen监听消息
        socket_tcp_server.listen(5)
        # 接受请求
        socket_con, addr = socket_tcp_server.accept()
        flag = 1

    #接收数据
    data = socket_con.recv(1024)
    print(str(data,'utf-8'))
    socket_con.sendall(bytes('对方已经接收消息',encoding='utf-8'))

    if data == 'exit':
        socket_con.close()
        flag = 0

#关闭连接
socket_tcp_server.close()