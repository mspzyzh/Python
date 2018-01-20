#!/usr/bin/env python
# -*- coding: utf-8 -*-

names = ('Michael','Bob','Tracy')   #依次打印出names元组
                                    #元组 tuple = () tuple一旦初始化就不能修改
for name in names:
    print name

i = [1,2,3,4,5,6,7,8,9,10]  #计算1-10的和
                            #列表 list = [] list是一种有序的集合，可以随时添加和删除其中的元素
sum = 0
for x in i:
    sum = sum + x
print sum

sum = 0
for x in range(101):    #range()函数，可以生成一个整数序列，比如range(5)生成的序列是从0开始小于5的整数
    sum = sum + x
print sum
