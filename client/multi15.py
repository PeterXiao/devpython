__author__ = 'Administrator'
import multiprocessing


def do_calculation(data):
    return data * 2



def start_process():
    print 'Starting', multiprocessing.current_process().name



if __name__ == '__main__':
    inputs = list(range(10))
    print 'Input   :', inputs



    builtin_outputs = map(do_calculation, inputs)  #返回一个隐射，lambda x:x*2
    print 'Built-in:', builtin_outputs



    pool_size = multiprocessing.cpu_count() * 2
    pool = multiprocessing.Pool(processes=pool_size, #进程池管理固定数量的进程，还能设定一个maxtasksperchild（从添加python2.7），任务可以完成之前
                                initializer=start_process,  #它会退出和更换一个新的工作进程，使闲置的资源被释放。
                                )
    pool_outputs = pool.map(do_calculation, inputs)  #   map方法与内置的map函数行为基本一致，在它会使进程阻塞与此直到结果返回。
    pool.close()  #关闭pool，使其不在接受新的任务。
    pool.join()  #结束当前任务,主进程阻塞等待子进程的退出， join方法要在close或terminate之后使用。



    print 'Pool    :', pool_outputs