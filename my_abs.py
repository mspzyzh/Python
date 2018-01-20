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


import math                             #在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标

def move(x, y, step, angle=0):          #angle=0为默认参数，必选参数在前，默认参数在后，否则Python的解释器会报错,默认参数必须指向不变对象!
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x,y = move(100, 100, 60, math.pi / 6)   #函数可以同时返回多个值，但其实就是一个tuple
r = move(100, 100, 60, math.pi / 6)
print x,y
print r


def func(a, b, c=0, *args, **kw):       #*args是可变参数，args接收的是一个tuple,**kw是关键字参数，kw接收的是一个dict。
                                        #可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))，关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
