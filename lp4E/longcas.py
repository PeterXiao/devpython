__author__ = 'Administrator'
'''def fprintf(file,fmt,*args):
    file.write(fmt % args)
fprintf(out ,"%d%s%f",42,"hello world",3.45)
'''
def foo(x,y,z):
    return x+y+z

#print(foo(x=100,y=1000,z=10000))
a = [1,2,3,4,5]
def square(items):
    for i ,x in enumerate(items):
        items[i]=x*x #原地修改item中的数据
#square(a);print(a)
def factor(a):
    d = 2
    while (d<=(a/2)):
        if ((a/d)*d==a):
            return ((a/d),d)
        d=d+1
    return (a,1)
'''x,y =factor(1243)
print(x)
print(y)'''
b = 12
def dr():
    b = 52
dr()
print(b)