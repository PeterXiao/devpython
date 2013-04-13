__author__ = 'Administrator'
def weishu(n):
    print(max(filter(lambda x : n%x == 0,range(100,999))))
weishu(1000156)
def last3(x,y,z):
    xx =[x]*y
    return reduce(lambda x,y:x*y%z,xx)
    print(last3(13,20,1000))
def getzero(n):
    k = 0
    for m in range(1,n+1):
        if m%25 == 0:
            k+=2
        elif m%5 == 0:
            k+=1
    return k
print(getzero(100))
