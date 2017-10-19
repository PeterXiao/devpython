#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test*.py

def funcx(x):
    print 'x is ',x
    x =2
    print  'changed local to', x

if __name__ == '__main__':
    x = 50
    funcx(x)
    print 'x os still ',x