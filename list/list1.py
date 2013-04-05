__author__ = 'Administrator'
'''
list 形式“[]”的数据集合，不同成员以“，”分隔，列表中可以包含任何数据类型，也可包含
另一个列表。
操作列表的方式，排序，添加，删除

元组的特性基本与list一致，不同的是，“（）”且元组的数据一旦确立就不能改变

'''
'''
lista=[1,2,3,'a','b','你好','nishi']

lista.append('f') #列表追加成员
lista.count()  #计算列表中出现的次数（包括成员列表存在相同的参数）
print(lista)
lista.extend(lista)# 列表追加另一个列表
lista.index('a') # 获得参数x在列表中的位置
lista.insert() #列表中插入数据
lista.pop() # 末尾删除并获取此删除的参数成员
lista.remove() #删除指定的成员
lista.reverse()# 将列表中的成员数据
'''

#eg

dic = {'apple':2,'orange':1}

dit =dic.copy()
print(dit)
dic['banana'] = 5
mu = dic.items()
print(mu)
dr = dic.pop('apple')
print(dr)
dr2 = dic.pop('apple',3)
print(dr2)
dic.keys()
dic.values()
dic.update({'banana':3})
print(dic)

print(dic['orange'])