# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson6.py
@Time    :   2020/03/28 18:27:57
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''

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
