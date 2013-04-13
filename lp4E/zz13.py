__author__ = 'Administrator'
def z13():
    #银行月息 0.63%，一人打算今后五年每年年底取款1000，正好取完，请问第一年应该取多少
    tl = 0
    for i in range(5):
        tl = (tl+1000)/(1+0.0063*12)
    print(tl)
z13()