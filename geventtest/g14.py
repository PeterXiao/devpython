__author__ = 'Administrator'
import gevent
from gevent.pool import Group
def talk(msg):
    for i in xrange(3):
        print(msg)


g1 = gevent.spawn(talk, 'bar')
g2 = gevent.spawn(talk, 'foo')
g3 = gevent.spawn(talk, 'fizz')



group = Group() #保持greenlet实例的组运行,连接到没个项目,在其完成后删除
group.add(g1)
group.add(g2)
group.join()



group.add(g3)
group.join()