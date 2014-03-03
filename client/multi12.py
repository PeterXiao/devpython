__author__ = 'Administrator'
import random
import multiprocessing
import time


class ActivePool(object):   #跟踪进程执行状态
    def __init__(self):
        super(ActivePool, self).__init__()  #保证公共父类仅被执行一次
        self.mgr = multiprocessing.Manager()  #进程间共享数据,支持的类型有list,dict,Namespace,Lock,RLock,Semaphore,BoundedSemaphore,Condition,Event,Queue,Value和Array
        self.active = self.mgr.list()
        self.lock = multiprocessing.Lock()
    def makeActive(self, name):
        with self.lock:
            self.active.append(name)
    def makeInactive(self, name):
        with self.lock:
            self.active.remove(name)
    def __str__(self):
        with self.lock:
            return str(self.active)



def worker(s, pool):
    name = multiprocessing.current_process().name
    with s:
        pool.makeActive(name)
        print 'Now running: %s' % str(pool)
        time.sleep(random.random())
        pool.makeInactive(name)



if __name__ == '__main__':
    pool = ActivePool()
    s = multiprocessing.Semaphore(3) #Semaphore用来控制对共享资源的访问数量，例如池的最大连接数，这里只有三个活动进程同时运行
    jobs = [
        multiprocessing.Process(target=worker, name=str(i), args=(s, pool))
        for i in range(10)
        ]



    for j in jobs:
        j.start()



    for j in jobs:
        j.join()
        print 'Now running: %s' % str(pool)