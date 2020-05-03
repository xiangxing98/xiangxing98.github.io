# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson22.py
@Time    :   2020/05/03 18:47:28
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''

# here put the import lib
from random import randint


def isEqual(num1, num2):
    if num1 < num2:
        print('too small')
        return False
    if num1 > num2:
        print('too big')
        return False
    if num1 == num2:
        print('bingo!')
        return True


# Guess
num = randint(1, 100)
print('Guess what I think?')
bingo = False
while bingo is False:
    answer = int(input())
    bingo = isEqual(answer, num)

# cd /f/Github/xiangxing98.github.io/Python_Learning
# python lesson22.py
