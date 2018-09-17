import socket

"""

* 创建socket,设置socket属性
	* client_udp = socket.socket(type=socket.SOCK_DGRAM)
* 设置目标IP地址和端口等属性; 
	* ip_port = ("172.16.5.236", 10086)
* 发送数据，用函数sendto(); 
	* msg = input("请输入要发送的信息：")
	* client_udp.sendto(bytes(msg, encoding="utf-8"), ip_port)
* 断开连接
	* client_udp.close()
"""
# 创建socket
socket_udp_client = socket.socket(type=socket.SOCK_DGRAM)
# 绑定ip地址和端口
ip_port = ('10.31.153.41', 10088)
# 发送数据
while True:
    data = input("请输入要发送的内容:\n")
    if data == '':
        continue

    if data == 'exit':
        break
    else:
        socket_udp_client.sendto(bytes(data, encoding='utf-8'), ip_port)
# 关闭链接
socket_udp_client.close()
