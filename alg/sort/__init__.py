# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# filename: *.py
from radixsort import  *
lst =[12, 23, 4, 5, 3, 2, 12, 81, 56, 95]

if __name__ == '__main__':
    sortedArray = radixsort(lst)
    print(sortedArray)