__author__ = 'Administrator'
import re
r1 =re.compile(r'(?i)hello')
r2 = re.compile(r'hello',re.I)
r3 = re.compile(r'hello',re.IGNORECASE)
#第三种方案最具有可读性，因此是最可维护

rr1 =re.compile(r'box')
if rr1.match('inbox'):
    print('match succeeds')
else:
    print('match fails')
if rr1.search('inbox'):
    print('search succeeds')
else:
    print('search fails')