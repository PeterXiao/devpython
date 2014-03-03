__author__ = 'Administrator'
import multiprocessing
import sys


def worker_with(lock, stream):
    with lock:
        stream.write('Lock acquired via with\n') #lock资源



def worker_no_with(lock, stream):
    lock.acquire() #获得资源
    try:
        stream.write('Lock acquired directly\n')
    finally:
        lock.release()  #释放资源



lock = multiprocessing.Lock() #需要多个进程之间共享一个单一的资源的情况下，可以使用Lock，以避免冲突的访问
w = multiprocessing.Process(target=worker_with, args=(lock, sys.stdout))
nw = multiprocessing.Process(target=worker_no_with, args=(lock, sys.stdout))



w.start()
nw.start()



w.join()
nw.join()