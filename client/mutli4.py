__author__ = 'Administrator'
import multiprocessing
import time


def slow_worker():
    print 'Starting worker'
    time.sleep(0.1)
    print 'Finished worker'






if __name__ == '__main__':
    p = multiprocessing.Process(target=slow_worker)
    print 'BEFORE:', p, p.is_alive()



    p.start()
    print 'DURING:', p, p.is_alive()



    p.terminate()  #发送结束进程信号
    print 'TERMINATED:', p, p.is_alive()



    p.join()  #更新状态以反应终止后的状态
    print 'JOINED:', p, p.is_alive()