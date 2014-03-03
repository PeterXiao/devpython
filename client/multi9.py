__author__ = 'Administrator'
import multiprocessing
import time
'''
执行结果：

dongwm@linux-dongwm:~> python test.py main:
waiting before calling Event.set() wait_for_event: starting wait_for_event_timeout: starting wait_for_event_timeout:
e.is_set()-> False main: event is set wait_for_event: e.is_set()-> True
'''

def wait_for_event(e):
    print 'wait_for_event: starting'
    e.wait()   #主线程将被阻塞，它将不会 再被分配时间片 直到现有的一些线程退出运行
    print 'wait_for_event: e.is_set()->', e.is_set()  #返回事件是否设置的布尔值



def wait_for_event_timeout(e, t):
    print 'wait_for_event_timeout: starting'
    e.wait(t)  #设置等待超时
    print 'wait_for_event_timeout: e.is_set()->', e.is_set()



if __name__ == '__main__':
    e = multiprocessing.Event()  #类似threading.Event,替代time.sleep(),用wait()和set()来精确控制线程
    w1 = multiprocessing.Process(name='block',
                                 target=wait_for_event,
                                 args=(e,))
    w1.start()



    w2 = multiprocessing.Process(name='non-block',
                                 target=wait_for_event_timeout,
                                 args=(e, 2))
    w2.start()



    print 'main: waiting before calling Event.set()'
    time.sleep(3)
    e.set()
    print 'main: event is set'