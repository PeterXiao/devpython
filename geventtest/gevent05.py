__author__ = 'Administrator'
import gevent
from gevent import Greenlet


class MyGreenlet(Greenlet):  #重载Greenlet类



    def __init__(self, message, n):
        Greenlet.__init__(self)
        self.message = message
        self.n = n



    def _run(self): #重写_run方法
        print(self.message)
        gevent.sleep(self.n)



g = MyGreenlet("Hi there!", 3)
g.start()
g.join()