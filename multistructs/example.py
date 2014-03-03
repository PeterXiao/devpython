__author__ = 'Administrator'
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

pool = ThreadPool(4)
#Sets the pool size to 4
