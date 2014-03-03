__author__ = 'Administrator'
import gevent
from gevent import Greenlet


def foo(message, n):
    gevent.sleep(n)
    print(message)



thread1 = Greenlet.spawn(foo, "Hello", 1)  #实例化Greenlet
thread2 = gevent.spawn(foo, "I live!", 2) #实例化gevent,其实也是创建Greenlet实例,只是包装了一下
thread3 = gevent.spawn(lambda x: (x+1), 2)  #一个lambda表达式



threads = [thread1, thread2, thread3]
gevent.joinall(threads) #等待所有greenlet完成