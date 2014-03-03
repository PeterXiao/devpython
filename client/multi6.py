__author__ = 'Administrator'
import multiprocessing


class Worker(multiprocessing.Process):   #最开始的例子也可以使用继承类的方式

    def run(self):
        print 'In %s' % self.name
        return



if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = Worker()
        jobs.append(p)
        p.start()
    for j in jobs:
        j.join()