__author__ = 'Administrator'
from gevent.server import StreamServer #StreamServer是一个通用的TCP服务器


def handle(socket, address):
    socket.send("Hello from a telnet!\n")
    for i in range(5):
        socket.send(str(i) + '\n') #给socket客户端发送数据
    socket.close() #关闭客户端连接



server = StreamServer(('127.0.0.1', 5000), handle) #当出现连接调用定义的方法handle
server.serve_forever()