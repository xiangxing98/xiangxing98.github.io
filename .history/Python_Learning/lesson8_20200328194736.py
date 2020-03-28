# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson8.py
@Time    :   2020/03/28 19:47:28
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''

# here put the import lib


# here put the import lib

# if
# age1 = input()
# age = int(age1)
age2 = int(input())
if age2 >= 18:
    print("你是个成年人了！")

# game
num = 10
print('Guess what I think?')
answer = int(input())
if answer < num:
    print('too small!')
if answer > num:
    print('too big!')
if answer == num:
    print('BINGO!')
