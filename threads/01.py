import threading
TOTAL = 0
MY_LOCK = threading.Lock()
class CountThread(threading.Thread):
    def run(self):
        global TOTAL
        for i in range(100000):
            MY_LOCK.acquire()
            TOTAL = TOTAL + 1
            MY_LOCK.release()
        print('%s\n' % (TOTAL))
#a = CountThread()
#b = CountThread()
#a.start()
#b.start()
from random import random

n=10**6
print sum(1 if random()**2 + random()**2 < 1 else 0 for i in range(n))*4.0/n