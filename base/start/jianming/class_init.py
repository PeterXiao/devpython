#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test*.py
class Person:
    def __init__(self,name = 'hie'):
        self.name =name
    def sayHi(self):
        print ' Hello,my name is ',self.name

if __name__ == '__main__':
    p =Person('Peter')
    p.sayHi()