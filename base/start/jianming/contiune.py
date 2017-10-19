#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test*.py
while True:
    s = raw_input('Enter something: ')
    if s == 'quit':
        break
    elif len(s) <3:
        continue
    print('Input is of sufficient lenth')