__author__ = 'Administrator'
import gevent
import random


def task(pid):
    gevent.sleep(random.randint(0,2)*0.001)
    print('Task', pid, 'done')



def synchronous():  #同步
    for i in range(1,10):
        task(i)



def asynchronous(): #异步
    threads = [gevent.spawn(task, i) for i in xrange(10)]
    gevent.joinall(threads)



print('Synchronous:')
synchronous()



print('Asynchronous:')
asynchronous()