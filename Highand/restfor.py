__author__ = 'Administrator'
import httplib2,socket

conn =httplib2.Http(".cache")
res,connect = conn.request("http://www.highand.cn/")

print(res)

