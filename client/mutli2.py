__author__ = 'Administrator'
import multiprocessing
import time
import sys


def daemon():
    p = multiprocessing.current_process()
    print 'Starting:', p.name, p.pid
    sys.stdout.flush()
    time.sleep(2)
    print 'Exiting :', p.name, p.pid
    sys.stdout.flush()



def non_daemon():  #默认情况下，主程序将不会退出，直到所有的孩子都已经退出
    p = multiprocessing.current_process()
    print 'Starting:', p.name, p.pid
    sys.stdout.flush()
    print 'Exiting :', p.name, p.pid
    sys.stdout.flush()



if __name__ == '__main__':
    d = multiprocessing.Process(name='daemon', target=daemon)
    d.daemon = True



    n = multiprocessing.Process(name='non-daemon', target=non_daemon)
    n.daemon = False   #默认是不是守护进程，以便通过真正轮流守护模式



    d.start()
    time.sleep(1)
    n.start()