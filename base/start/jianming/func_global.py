#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test*.py


def func():
    global x

    print('x is', x)
    x = 2
    print('Changed local x to', x)


if __name__ == '__main__':
    x = 50
    func()
    print('Value of x is', x)
