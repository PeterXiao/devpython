#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test*.py
import time

def tryfin():
    try:
        f = file('poem.txt')
        while True:  # our usual file-reading idiom
            line = f.readline()
            if len(line) == 0:
                break
            time.sleep(2)
            print line,
    finally:
        f.close()
        print 'Cleaning up...closed the file'


if __name__ == '__main__':
    tryfin()