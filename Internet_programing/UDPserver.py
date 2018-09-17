import socket

"""
　　1、创建一个socket，用函数socket()； 
　　2、设置socket属性，用函数setsockopt();* 可选 
　　3、绑定IP地址、端口等信息到socket上，用函数bind();* 可选 
　　4、设置对方的IP地址和端口等属性; 
　　5、发送数据，用函数sendto(); 
　　6、关闭网络连接；
"""

# 创建socket对象
socket_udp_server = socket.socket(type=socket.SOCK_DGRAM)
# 绑定ip和端口号
ip_port = ('10.31.153.41', 10088)
socket_udp_server.bind(ip_port)
# 接收消息

while True:
    data, addr = socket_udp_server.recvfrom(1024)
    print(str(data, encoding='utf-8'))

# 关闭连接
socket_udp_server.close()
