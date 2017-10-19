#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：radix_sort*.py

def radixsort(lst):
    RADIX = 10
    maxLength = False
    tmp, placement = -1, 1
    while not maxLength:
        maxLength = True
        # declare and intialize buckets
        buckets = [list() for _ in range(RADIX)]

        # split lst between lists
        for i in lst:
            tmp = i // placement
            buckets[tmp % RADIX].append(i)
            if maxLength and tmp > 0:
                maxLength = False

        # empty lists into lst array
        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                lst[a] = i
                a += 1

        # move to next

        placement *= RADIX

    return lst


import math


def radix_sort(lists, radix=10):
    k = int(math.ceil(math.log(max(lists), radix)))
    bucket = [[] for i in range(radix)]
    for i in range(1, k + 1):
        for j in lists:
            bucket[j / (radix ** (i - 1)) % (radix ** i)].append(j)
        del lists[:]
        for z in bucket:
            lists += z
            del z[:]
    return lists
