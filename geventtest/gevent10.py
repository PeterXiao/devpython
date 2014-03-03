__author__ = 'Administrator'
import gevent
from gevent.event import AsyncResult


a = AsyncResult() #保存一个值或者一个异常的事件实例



def setter():
    gevent.sleep(3)  #3秒后唤起所有线程的a的值
    a.set() #保存值,唤起等待线程



def waiter():
    a.get() # 3秒后get方法不再阻塞,返回存贮的值或者异常
    print 'I live!'



gevent.joinall([
    gevent.spawn(setter),
    gevent.spawn(waiter),
])