__author__ = 'Administrator'
from math import sqrt
def shu():
    t = range(1,10)
    for i in t:
        for j in t:
            m = i*1100+j*11
            n = int(sqrt(m))
            if m ==n*n and i !=j:
                print(m)
shu()