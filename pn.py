#!/usr/bin/env python
# -*- coding: utf-8 -*-

def is_ss(n):   #判断这个数是不是素数
    if n == 1:  #1不是素数
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return True
    return False

print filter(is_ss, [x for x in range(1, 101)]) #筛选并打印出1-100中非素数
