__author__ = 'Administrator'
import time
import gevent
from gevent import select
#类似于内置的select.select()实现
# (请关注http://www.dongwm.com/archives/guanyuselectyanjiu/),
# 只是将线程操作改成了greenlet
"""
执行结果:

dongwm@localhost ~ $ python test.py
(‘Hey lets do some stuff while the greenlets poll, at’, ‘at 0.0 seconds’)
 #因为gr1和gr2开始是阻塞的,gr3直接打印
 (‘Started Polling: ‘, ‘at 0.0 seconds’)
 (‘Started Polling: ‘, ‘at 0.0 seconds’) (‘Ended Polling: ‘, ‘at 2.0 seconds’)
 (‘Ended Polling: ‘, ‘at 2.0 seconds’)
"""

start = time.time()
tic = lambda: 'at %1.1f seconds' % (time.time() - start)



def gr1():
    print('Started Polling: ', tic())
    select.select([], [], [], 2)  #参数分别是,等待的可读列表,等待的可写列表,等待的可执行列表,超时时间(这里是2秒)
    print('Ended Polling: ', tic())



def gr2():
    print('Started Polling: ', tic())
    select.select([], [], [], 2)
    print('Ended Polling: ', tic())



def gr3():
    print("Hey lets do some stuff while the greenlets poll, at", tic())
    gevent.sleep(1)



gevent.joinall([
    gevent.spawn(gr1),
    gevent.spawn(gr2),
    gevent.spawn(gr3),
])