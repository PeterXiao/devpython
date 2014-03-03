__author__ = 'Administrator'
from gevent.pool import Pool


class SocketPool(object):



    def __init__(self):
        self.pool = Pool(1000)  #设置池容量1000
        self.pool.start()



    def listen(self, socket):
        while True:
            socket.recv()



    def add_handler(self, socket):
        if self.pool.full(): #容量慢报错
            raise Exception("At maximum pool size")
        else: #否则执行在新的grenlet里面执行listen方法
            self.pool.spawn(self.listen, socket)



    def shutdown(self):
        self.pool.kill() #关闭pool