__author__ = 'Administrator'
def yanghuisanjiao():
    g = lambda x,y:(y==1 or y == x+1) and 1 or g(x-1,y-1)+g(x-1,y)
    for m in range(1,13):
        print(' '*2*(13-m))
        for n in range(1,m+2):
            print(str(g(m,n)).center(4),)
        print(" ")
#yanghuisanjiao
def ddg():
    def g(n,k):
        d = n
        s = ""
        while d!=0:
            d,f = divmod(d,k)
            s = str(f)+s
        return s
    print(g(234,2)
