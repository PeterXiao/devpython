__author__ = 'Administrator'
import multiprocessing
import time


def worker():
    name = multiprocessing.current_process().name  #当前进程名字
    print name, 'Starting'
    time.sleep(2)
    print name, 'Exiting'



def my_service():
    name = multiprocessing.current_process().name
    print name, 'Starting'
    time.sleep(3)
    print name, 'Exiting'



if __name__ == '__main__':
    service = multiprocessing.Process(name='my_service', target=my_service) #使用自定义的函数名
    worker_1 = multiprocessing.Process(name='worker 1', target=worker)
    worker_2 = multiprocessing.Process(target=worker) # use default name  #使用默认的函数名，即Process-3



    worker_1.start()
    worker_2.start()
    service.start()