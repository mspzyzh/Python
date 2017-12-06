#!/usr/bin/python
# -*- coding: utf-8 -*-
age = int(raw_input('Your age '))
print 'your age is', age
if age >= 18:
    print 'adult'
elif age >= 6:
    print 'teeenager'
else:
    print 'kid'
