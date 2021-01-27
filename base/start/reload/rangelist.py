#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author xiaoyulong07@outlook.com
# @version 3

print(range(100))
print(list(range(100)))
# for i in range(100):
#     print(i)
print(range(2,100))
print(list(range(2,100)))
print(list(range(2,100,2)))
sum = 0
for i in range(1,100,2):
    sum = sum+i
print(sum)