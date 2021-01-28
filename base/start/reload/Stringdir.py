#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author xiaoyulong07@outlook.com
# @version 3

a="python"
b='python'
c='''python'''
print(a,id(a))
print(b,id(b))
print(c,id(c))

def printf(a):
    print(a,id(a))
print("Test hello world")

s = 'hello , Python'
print(s.replace('Python', 'Java'))

lst =['hello', 'Python', 'Java']
print('|'.join(lst))
print(''.join(lst))

print('sword'>'sworc')
print(ord('萧'))
print(chr(33831))

# == 比较的neirong
# is 比较的是内存地址
#python 字符串驻留机制
#字符串切片之后产生新的字符串，字符串是不可变类型，列表是可变类型

s='hello,Python'
s1=s[:5]
print(s1)
s2=s[6:]
print(s2)

s3=s1+'!'+s2

print(s3)

print(id(s))
print(id(s2))
print(id(s3))
print(id(lst))

#格式化字符串： %s %d %f  字符串 整数 浮点
#{} 做占位符
#f'{}'格式化
# %10d %.3f  %10.3f
#'{0:.3}'.format(floatnum)

#a计算机传输byte b计算机，再转换回来
