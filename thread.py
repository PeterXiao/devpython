__author__ = 'Administrator'
#!/user/bin/env python
#-*- encoding:utf-8 -*-
import socket
import thread,threading

sockIndex = 1

def connToServer ():
    global sockIndex
    #创建一个socket连接到127.0.0.1:8081，并发送内容
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(("127.0.0.1", 8081))
    conn.send("hi."+ str(sockIndex))
    print (sockIndex)
    sockIndex = sockIndex + 1
    while True:
    #等待服务端返回数据，并输出
        rev = conn.recv(1024)
        print( 'get server msg:' + str(rev))
        break
threads = []
times = 20000
#并发
for i in range(0,times):
    t = threading.Thread(target=connToServer())
    threads.append(t)
for i in range(0,times):
    threads[i].start()
for i in range(0,times):
    threads[i].join()

