# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# filename: *.py
from random import random,randint

from alg.sort.selectsort import select_sort
from alg.sort.shellsort import shell_sort
from radixsort import  *

# from alg.sort.bubble_sort import bubble_sort
# from alg.sort.shellsort import shell_sort
# from alg.sort.selectsort import select_sort

lst =[12, 23, 4, 5, 3, 2, 12, 81, 56, 95]

if __name__ == '__main__':
    sortedArray = radixsort(lst)
    print(sortedArray)
    lsts=[]
    lsts =[randint(1,15000000) for i in range(15000000)]
    print("lsts:",lsts)
    # list1 =[22, 12, 14, 13, 41, 41, 17, 25, 39, 40, 16, 38, 15, 50, 15, 3, 3, 46, 22, 28, 13, 11, 25, 25, 32, 43, 34, 50, 46, 35, 42, 31, 46, 50, 49, 13, 1, 4, 38, 35, 15, 20, 15, 7, 30, 48, 29, 16, 38]
    # list =[]
    # for i in lsts:
    #        list.append(randint(1,50))
    print(list)
    # print(select_sort(lsts))
    # reload(list)
    shell_sort(lsts)
    # for i in range(100):
    #     print(randint(1, 50))
