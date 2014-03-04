__author__ = 'Administrator'
# A program to simulate selling tickets in multi-thread way
# Written by Vamei

import threading
import time
import os

# This function could be any function to do other chores.
def doChore():
    time.sleep(0.5)

# Function for each thread
class BoothThread(threading.Thread):
    def __init__(self, tid, monitor):
        self.tid          = tid
        self.monitor = monitor
        threading.Thread.__init__(self)
    def run(self):
        while True:
            monitor['lock'].acquire()                          # Lock; or wait if other thread is holding the lock
            if monitor['tick'] != 0:
                monitor['tick'] = monitor['tick'] - 1          # Sell tickets
                print(self.tid,':now left:',monitor['tick'])   # Tickets left
                doChore()                                      # Other critical operations
            else:
                print("Thread_id",self.tid," No more tickets")
                os._exit(0)                                    # Exit the whole process immediately
            monitor['lock'].release()                          # Unblock
            doChore()                                          # Non-critical operations

# Start of the main function
monitor = {'tick':100, 'lock':threading.Lock()}

# Start 10 threads
for k in range(10):
    new_thread = BoothThread(k, monitor)
    new_thread.start()
	
	
"""
我们自己定义了一个类BoothThread, 这个类继承自thread.Threading类。
然后我们把上面的booth()所进行的操作统统放入到BoothThread类的run()方法中。
注意，我们没有使用全局变量声明global，而是使用了一个词典monitor存放全局变量，
然后把词典作为参数传递给线程函数。由于词典是可变数据对象，所以当它被传递给函数的时候，
函数所使用的依然是同一个对象，相当于被多个线程所共享。这也是多线程乃至于多进程编程的一个技巧 
(应尽量避免上面的global声明的用法，因为它并不适用于windows平台)

threading.Thread对象： 我们已经介绍了该对象的start()和run(), 此外：

join()方法，调用该方法的线程将等待直到改Thread对象完成，再恢复运行。这与进程间调用wait()函数相类似。
 

下面的对象用于处理多线程同步。对象一旦被建立，可以被多个线程共享，
并根据情况阻塞某些进程。请与Linux多线程与同步中的同步工具参照阅读。

threading.Lock对象: mutex, 有acquire()和release()方法。

threading.Condition对象: condition variable，建立该对象时，
会包含一个Lock对象 (因为condition variable总是和mutex一起使用)。
可以对Condition对象调用acquire()和release()方法，以控制潜在的Lock对象。此外:

wait()方法，相当于cond_wait()
notify_all()，相当与cond_broadcast()
nofify()，与notify_all()功能类似，但只唤醒一个等待的线程，而不是全部
threading.Semaphore对象: semaphore，也就是计数锁(semaphore传统意义上是一种进程间同步工具，
见Linux进程间通信)。创建对象的时候，
可以传递一个整数作为计数上限 (sema = threading.Semaphore(5))。
它与Lock类似，也有Lock的两个方法。
threading.Event对象: 与threading.Condition相类似，
相当于没有潜在的Lock保护的condition variable。
对象有True和False两个状态。可以多个线程使用wait()等待，
直到某个线程调用该对象的set()方法，将对象设置为True。
线程可以调用对象的clear()方法来重置对象为False状态。

"""