#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test*.py
from past.builtins import apply


def function(a):
    print(a)


# def function(a, b):
#     print(a+ b)


if __name__ == '__main__':
    apply(function, (123456, 123569))
    #function((123456, 123569), (123456, 123569))
    # apply(function, (123456, 123569), (123456, 123569))
