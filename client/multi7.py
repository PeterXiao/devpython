__author__ = 'Administrator'
import multiprocessing
'''
   注：Queue建构在系统的Pipe之上，但是实际上进程并不是直接将对象写入到Pipe里面，而是先写入一个本地的buffer，

再由一个专门 的feed线程将其放入Pipe当中。读取端则是直接从Pipe当中读出对象。之所以有这样一个feed线程，

是为了能够提供Queue接口函数所需要的 put的超时控制。但是由于这个feed线程的存在，mp.Queue提供了几个额外的函数来控制它，

一个函数close来停止该线程，以及 join_thread来join该线程。close同时负责把所有在buffer当中的对象刷新到Pipe当中

'''

class MyFancyClass(object):



    def __init__(self, name):
        self.name = name



    def do_something(self):
        proc_name = multiprocessing.current_process().name
        print 'Doing something fancy in %s for %s!' % (proc_name, self.name)



def worker(q):
    obj = q.get()   #获取队列
    obj.do_something()



if __name__ == '__main__':
    queue = multiprocessing.Queue() #Queue基本属于Queue.Queue模块的复制,他主要用来做进程间的通信



    p = multiprocessing.Process(target=worker, args=(queue,))
    p.start()



    queue.put(MyFancyClass('Fancy Dan'))



    queue.close()
    queue.join_thread()  #
    p.join()   #阻塞直到queue中的所有的task都被处理（即task_done方法被调用）