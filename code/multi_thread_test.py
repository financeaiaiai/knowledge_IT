#!/usr/bin/env python
#!coding:utf-8
'''
author: dinghewu
date: 2018/11/11 @ 14:40
python 3.6.2
'''
import time
from multiprocessing import process
from threading import Thread
import queue

def func(num):
    num = num + 100
    time.sleep(1)
    print(num)
    num = num - 100
    time.sleep(1)
    print(num)

if __name__ == '__main__':
    start=time.time()
    lst=[1,2,3,4,5,6]
    for ele in lst:
        func(ele)
    print('cost:%d'%(time.time()-start))
