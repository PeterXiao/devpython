__author__ = 'Administrator'
re = iter(range(5))
def e01():
   for i in range(100):
         print re.next()
   print 'HaHaHaHa'


def e02():
   try:
        for i in range(100):
            print re.next()
   except StopIteration:
        print 'here is end ',i
   print 'HaHaHaHa'

#if '__name__' == '__main__':
e02()
"""
try:
    ...
except exception1:
    ...
except exception2:
    ...
except:
    ...
else:
    ...
finally:
    ...
"""