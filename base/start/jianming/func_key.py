#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test*.py

def func(a, b=5, c=10):
    print 'a is', a, 'and b is', b, 'and c is', c


if __name__ == '__main__':
    func(3, 7)
    func(25, c=24)
    func(c=50, a=100)