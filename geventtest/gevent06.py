__author__ = 'Administrator'
import gevent


def win():
    return 'You win!'



def fail():
    raise Exception('You fail at failing.')



winner = gevent.spawn(win)
loser = gevent.spawn(fail)



print(winner.started) # started表示的Greenlet是否已经开始,返回布尔值
print(loser.started)  # True



try:
    gevent.joinall([winner, loser])
except Exception as e:
    print('This will never be reached')



print(winner.value) # value表示greenlet实例返回值:'You win!'
print(loser.value)  # None



print(winner.ready()) # 是否已停止Greenlet的布尔值,True
print(loser.ready())  # True



print(winner.successful()) # 表示的Greenlet是否已成功停止，而不是抛出异常,True
print(loser.successful())  # False
print(loser.exception) #打印异常的报错信息