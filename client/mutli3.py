__author__ = 'Administrator'
import multiprocessing
import time
import sys


def daemon():
    print 'Starting:', multiprocessing.current_process().name
    time.sleep(2)
    print 'Exiting :', multiprocessing.current_process().name



def non_daemon():
    print 'Starting:', multiprocessing.current_process().name
    print 'Exiting :', multiprocessing.current_process().name



if __name__ == '__main__':
    d = multiprocessing.Process(name='daemon', target=daemon)
    d.daemon = True



    n = multiprocessing.Process(name='non-daemon', target=non_daemon)
    n.daemon = False



    d.start()
    time.sleep(1)
    n.start()



    d.join() #会使主调线程堵塞，直到被调用线程运行结束或超时,join函数可以设置超时， 如果进程在超时期限内没有完成就返回 比如join(1)，可以通过d.is_alive()查看进程是否存活
    n.join()