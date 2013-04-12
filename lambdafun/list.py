__author__ = 'Administrator'
y =  [x ** 2 for x in range(10)]
print(y)

y =list(map((lambda x: x ** 2), range(10)))
print(y)

y = [x for x in range(5) if x % 2 == 0] #list(filter((lambda x: x % 2 == 0), range(5)))

'''
for x in range(5):
...     if x % 2 == 0:
...         res.append(x)
'''
res = list( map((lambda x: x**2), filter((lambda x: x % 2 == 0), range(10))) )
print(res)

res = [x + y for x in [0, 1, 2] for y in [100, 200, 300]]
'''
for x in [0, 1, 2]:
...     for y in [100, 200, 300]:
...         res.append(x + y)
...

'''

z = [x + y for x in 'spam' for y in 'SPAM']
print(z)

print([(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1])
'''
>>> for x in range(5):
...     if x % 2 == 0:
...         for y in range(5):
...             if y % 2 == 1:
...                 res.append((x, y))

'''

'''
>>> M = [[1, 2, 3],
...      [4, 5, 6],
...      [7, 8, 9]]

>>> N = [[2, 2, 2],
...      [3, 3, 3],
...      [4, 4, 4]]


>>> M[1]
[4, 5, 6]

>>> M[1][2]
6


>>> [row[1] for row in M]
[2, 5, 8]

>>> [M[row][1] for row in (0, 1, 2)]
[2, 5, 8]


>>> [M[i][i] for i in range(len(M))]
[1, 5, 9]


>>> [M[row][col] * N[row][col] for row in range(3) for col in range(3)]
[2, 4, 6, 12, 15, 18, 28, 32, 36]

>>> [[M[row][col] * N[row][col] for col in range(3)] for row in range(3)]
[[2, 4, 6], [12, 15, 18], [28, 32, 36]]



>>> res = []
>>> for row in range(3):
...     tmp = []
...     for col in range(3):
...         tmp.append(M[row][col] * N[row][col])
...     res.append(tmp)
...
>>> res
[[2, 4, 6], [12, 15, 18], [28, 32, 36]]


'''

#open('myfile').readlines()
#[line.rstrip() for line in open('myfile').readlines()] #line.rstrip() for line in open('myfile')]
#list(map((lambda line: line.rstrip()), open('myfile')))
'''
>>> [x ** 2 for x in range(4)]          # List comprehension: build a list
[0, 1, 4, 9]

>>> (x ** 2 for x in range(4))          # Generator expression: make an iterable
<generator object at 0x011DC648>

'''

'''
>>> G = (x ** 2 for x in range(4))
>>> next(G)
0
>>> next(G)
1
>>> next(G)
4
>>> next(G)
9
>>> next(G)


'''

'''
>>> for num in (x ** 2 for x in range(4)):
...     print('%s, %s' % (num, num / 2.0))
...
0, 0.0
1, 0.5
4, 2.0
9, 4.5

'''