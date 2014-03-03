__author__ = 'Administrator'
import multiprocessing
import time


class Consumer(multiprocessing.Process):



    def __init__(self, task_queue, result_queue):
        multiprocessing.Process.__init__(self)
        self.task_queue = task_queue
        self.result_queue = result_queue



    def run(self):
        proc_name = self.name
        while True:
            next_task = self.task_queue.get()  #获取队列
            if next_task is None:
                print '%s: Exiting' % proc_name
                self.task_queue.task_done()  #向任务已经完成的队列发送一个信号
                break
            print '%s: %s' % (proc_name, next_task)
            answer = next_task() #执行队列的那个类
            self.task_queue.task_done()
            self.result_queue.put(answer)
        return



class Task(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __call__(self):
        time.sleep(0.1) # 保证这部分正常执行
        return '%s * %s = %s' % (self.a, self.b, self.a * self.b)
    def __str__(self):
        return '%s * %s' % (self.a, self.b)  #元类计算结果



if __name__ == '__main__':
    tasks = multiprocessing.JoinableQueue()  #JoinableQueue 是 Queue的子类，增加了task_done()和join()方法
    results = multiprocessing.Queue()



    num_consumers = multiprocessing.cpu_count() * 2  #创建消费者，cpu个数的2倍
    print 'Creating %d consumers' % num_consumers
    consumers = [ Consumer(tasks, results)
                  for i in xrange(num_consumers) ]
    for w in consumers:
        w.start()



    num_jobs = 10
    for i in xrange(num_jobs):
        tasks.put(Task(i, i))  #创建10个job



    for i in xrange(num_consumers):  #为每个消费者添加队列结束标记
        tasks.put(None)
    tasks.join()  #等待所有tasks完成



    while num_jobs:
        result = results.get()
        print 'Result:', result  #打印结果
        num_jobs -= 1