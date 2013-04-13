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
def z14():
    