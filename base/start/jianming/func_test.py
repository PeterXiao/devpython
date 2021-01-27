#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test*.py

def sayHello():
    print('Hello')


def printMax(a,b):
    if a>b:
        print(a, 'is maxinum')
    else:
        print(b, 'is maxinum')


if __name__=='__main__':
    sayHello()
    printMax(1,1)