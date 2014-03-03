__author__ = 'Administrator'
import gevent
from gevent import getcurrent
from gevent.pool import Group


group = Group()



def hello_from(n):
    print('Size of group', len(group))
    print('Hello from Greenlet %s' % id(getcurrent()))  #获取当前gevent实例的id



group.map(hello_from, xrange(3)) #map迭代方法,参数为方法和其参数



def intensive(n):
    gevent.sleep(3 - n)
    return 'task', n



print('Ordered')



ogroup = Group()
for i in ogroup.imap(intensive, xrange(3)):  #相当于 itertools.imap,返回一个迭代器, 它是调用了一个其值在输入迭代器上的函数, 返回结果. 它类似于函数 map() , 只是前者在
#任意输入迭代器结束后就停止(而不是插入None值来补全所有的输入)
    print(i)



print('Unordered')



igroup = Group()
for i in igroup.imap_unordered(intensive, xrange(3)):
    print(i)