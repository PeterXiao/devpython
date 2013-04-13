__author__ = 'Administrator'
def fabolacci(n):
    #斐波拉契数列
    def filie(x):
        a,b,t=1,1,0
        if x==1 or x ==2:return 1
        while t!=x-2:
            a,b,t=b,a+b,t+1
        return b
    for i in range(1,n):
        print(filie(i))
fabolacci(10)