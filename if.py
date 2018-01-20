#!/usr/bin/env python
# -*- coding: utf-8 -*-
age = int(raw_input('Your age '))   #raw_input 输入函数 raw_input()读取的内容永远以字符串的形式返回，把字符串和整数比较就不会得到期待的结果，必须先用int()把字符串转换为我们想要的整型
print 'your age is', age
if age >= 18:
    print 'adult'
elif age >= 6:
    print 'teeenager'
else:
    print 'kid'
