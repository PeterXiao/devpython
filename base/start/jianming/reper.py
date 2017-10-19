#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test*.py

def defrepr(x):
    return repr(x)


def powersum(power, *args):
    '''Return the sum of each argument raised to specified power.'''
    total = 0
    for i in args:
        total += pow(i, power)
    return total

if __name__ == '__main__':
    i = []
    i.append('item')
    print i
    print defrepr(i)
    print repr(i)