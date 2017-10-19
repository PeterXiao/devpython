#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test*.py

class Person:
    def sayHi(self):
        print('Hello,how are you？')
    pass

if __name__ == '__main__':
    p = Person()
    print (p)
    p.sayHi()