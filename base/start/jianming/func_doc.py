#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test*.py

def printMax(x, y):
    '''Prints the maximum of two numbers.

    The two values must be integers.'''
    x = int(x) # convert to integers, if possible
    y = int(y)

    if x > y:
        print x, 'is maximum'
    else:
        print y, 'is maximum'



if __name__ == '__main__':
    printMax(3, 5)
    print printMax.__doc__