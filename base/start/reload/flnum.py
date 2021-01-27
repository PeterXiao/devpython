#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author xiaoyulong07@outlook.com
# @version 3

for item in range(100, 1000):

     ge = item%10
     shi = (item//10)%10
     bai = (item//100)%10
     # print(item)
     # print(ge, shi, bai)
     if ge**3+ shi**3+ bai**3 == item:
         print(item)