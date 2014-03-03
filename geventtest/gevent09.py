__author__ = 'Administrator'
import gevent
from gevent import Timeout


def wait():
    gevent.sleep(2)



timer = Timeout(1).start()
thread1 = gevent.spawn(wait)  #这种超时类型前面讲过



try:
    thread1.join(timeout=timer)
except Timeout:
    print('Thread 1 timed out')



timer = Timeout.start_new(1) #start_new是一个快捷方式
thread2 = gevent.spawn(wait)



try:
    thread2.get(timeout=timer) #get返回greenlet的结果,包含异常
except Timeout:
    print('Thread 2 timed out')



try:
    gevent.with_timeout(1, wait) #如果超时前返回异常,取消这个方法
except Timeout:
    print('Thread 3 timed out')