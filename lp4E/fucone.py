__author__ = 'Administrator'
principal = 1000 #初始金额
rate = 0.05 #利率
numberyears = int(input("Years:")) #年数
year= 1
while year <= numberyears:
    principal = principal*(1+rate)
    print(year,principal)
    year +=1