#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：bubble_sort*.py

def bubble_sort(lst):
    #bubble_sort
    count = len(lst)
    for i in range(0,count):
        for j in range(i+1 ,count):
            if lst[i] >lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

