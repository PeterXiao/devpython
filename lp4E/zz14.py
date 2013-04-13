__author__ = 'Administrator'
def z15():
    '''
    五人同时捕鱼，啊先将多余的鱼分成五份，把多余的一条扔了，拿走自己的一份，bcde都这样拿，问鱼最少多少条

    '''
    n= 1
    nn= 5
    flag = 0
    while flag ==0:
        n+=5
        s = n
        for i in range(5):
            s,y =divmod(s-1,5)
            if y == 0:
                s*=4
                flag =1
            else:
                flag = 0
                break
    print(n)
#z15()
def z16():
    '''
    卖鱼，第一次卖了二分之一加二分之一条
         第二次卖了三分之一加三分之一条
         。。。
         第四次卖了四分之一加四分之一条
         余下十一条，问一开始是多少条
    '''
    n = 23
    nn =5
    falg =0
    while falg == 0:
        n+=2
        ss=n
        for i in range(1,5):
            s,y=divmod(ss+1,(i+1))
            if y ==0:
                ss-=s
                flag=1
            else:
                flag = 0
                break
    print(n)


z16()