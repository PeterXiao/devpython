__author__ = 'Administrator'
import math
a = [-3,5,2,-10,7,8]
b = 'abc'
c = [2*s for s in a]
for i in a:
    print(i)
d =[s for s in a if s>=0 ]
e =[(x,y)for x in a
    for y in b
    if x > 0]
#f = [(1,2),(3,4),(5,6)]