__author__ = 'Administrator'
import sys
print(sys.getrecursionlimit())
s = "for i in range(0,10):print(i)"
c = compile(s,'','exec')
exec(c)
