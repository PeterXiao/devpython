__author__ = 'luozi'
from twisted.internet import reactor
import time

def timefoit(func):
    def wrapper():
        start =time.clock()
        func()
        end =time.clock()
        return wrapper
    return wrapper

def  reactorrun():
    print('running reactor ...')
    reactor.run()
    print('reactor stopped')


def printTime():
    print('Current time is,',time.strftime("%H:%M:%S"))

def stopReactor():
    print('stop reactor')
    reactor.stop()

def test():
    for i in range(10):
       reactor.callLater(i,printTime)
    reactor.run()
    reactor.run(1,stopReactor())

test()
#reactorrun()