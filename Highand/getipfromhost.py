__author__ = 'Administrator'
##@小五义 http://www.cnblogs.com/xiaowuyi
import socket
host=input('host:')
result=socket.getaddrinfo(host,None)
counter=0
for i in result:
    print( "%-2d:%s"%(counter,i[4]))
    counter+=1