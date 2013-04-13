__author__ = 'Administrator'
def pingjun():
    '''
    唱歌大赛，去掉最高与最低分得到平均分
    '''
    def g(n):
        x = max(n)
        nn= min(n)
        print("最高分",x)
        print("最低分",nn)
        print("平均分",(sum(n)-x-nn)/(len(n)-2))
    m =[1,2,3,4,5,3,4,6,9]
    g(m)
pingjun()