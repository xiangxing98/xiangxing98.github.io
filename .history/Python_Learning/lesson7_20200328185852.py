# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson7.py
@Time    :   2020/03/28 18:58:36
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''

# here put the import lib

# bool
a = 1 < 3
print(a)
b = 1
c = 3
print(b > c)

# Game
num = 10
print('Guess what I think?')
answer = int(input())

result = answer < num
print('too small?')
print(result)

result = answer > num
print('too big?')
print(result)

result = answer == num
print('equal?')
print(result)
