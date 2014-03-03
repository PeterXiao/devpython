__author__ = 'Administrator'
import multiprocessing
import time


def stage_1(cond):  #执行工作的第一阶段，然后通知继续阶段2”
    name = multiprocessing.current_process().name
    print 'Starting', name
    with cond:
        print '%s done and ready for stage 2' % name
        cond.notify_all()   #唤醒所有挂起的线程（如果存在挂起的线程），但是这些方法不会释放所占用的琐



def stage_2(cond):  #告诉我们阶段1完成的情况下等待
    name = multiprocessing.current_process().name
    print 'Starting', name
    with cond:
        cond.wait()  #释放内部所占用的琐，同时线程被挂起，直至接收到通知被唤醒或超时（如果提供了timeout参数的话）。
                     #当线程被唤醒并重新占有琐的时候，程序才会继续执行下去。
        print '%s running' % name



if __name__ == '__main__':
    condition = multiprocessing.Condition() #它提供了比Lock, RLock更高级的功能，允许我们能够控制复杂的线程同步问题
    s1 = multiprocessing.Process(name='s1', target=stage_1, args=(condition,))
    s2_clients = [
        multiprocessing.Process(name='stage_2[%d]' % i, target=stage_2, args=(condition,))
        for i in range(1, 3)
        ]



    for c in s2_clients:
        c.start()
        time.sleep(1)
    s1.start()



    s1.join()
    for c in s2_clients:
        c.join()