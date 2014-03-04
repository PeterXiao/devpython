__author__ = 'Administrator'
bigmuls = lambda xs,ys: filter(lambda (x,y):x*y > 25, combine(xs,ys))
combine = lambda xs,ys: map(None, xs*len(ys), dupelms(ys,len(xs)))
dupelms = lambda lst,n: reduce(lambda s,t:s+t, map(lambda l,n=n: [l]*n, lst))
print bigmuls((1,2,3,4),(10,15,3,22))

# Nested loop procedural style for finding big products
xs = (1,2,3,4)
ys = (10,15,3,22)
bigmuls2 = []
# ...more stuff...
for x in xs:
    for y in ys:
        # ...more stuff...
        if x*y > 25:
            bigmuls2.append((x,y))
            # ...more stuff...
# ...more stuff...
print bigmuls2
'''
在函数中绝对没有改变变量的值。
这样就不可能在之后的代码（或者从之前的代码）中产生不可预期的副作用。
显然，在函数中没有副作用，并不能保证代码的正确性，但它仍然是一个优点。
'''
print [(x,y) for x in (1,2,3,4) for y in (10,15,3,22) if x*y > 25]