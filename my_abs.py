#!/usr/bin/env python
# -*- coding: utf-8 -*-
def my_abs(x):                          #定义一个abs函数
    if not isinstance(x,(int,float)):   #对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance实现
        raise TypeError('bad operand type')
    if x >= 0:
        return x                        #如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return
    else:
        return -x

def nop():                              #如果想定义一个什么事也不做的空函数，可以用pass语句，让代码能运行起来
    pass

