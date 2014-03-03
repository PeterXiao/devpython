__author__ = 'Administrator'
from gevent import sleep
from gevent.pool import Pool
from gevent.coros import BoundedSemaphore


sem = BoundedSemaphore(2) #设定对共享资源的访问数量



def worker1(n):
    sem.acquire() #获取资源
    print('Worker %i acquired semaphore' % n)
    sleep(0)
    sem.release()  #释放资源
    print('Worker %i released semaphore' % n)



def worker2(n):
    with sem: #使用with关键字
        print('Worker %i acquired semaphore' % n)
        sleep(0)
    print('Worker %i released semaphore' % n)



pool = Pool()
pool.map(worker1, xrange(0,2))
pool.map(worker2, xrange(3,6))