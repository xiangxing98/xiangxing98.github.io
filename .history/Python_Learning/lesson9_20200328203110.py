# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson9.py
@Time    :   2020/03/28 20:29:00
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''

# here put the import lib

# while
a = 1             # 为了后面的条件能满足，先把a设为1
while a != 0:     # 如果a不等于0就循环（1不等于0）
    print("please input")
    a = int(input())     # 在循环内部获取输入，改变a的值（想想看不改会怎样？）
print("over")

# game-While
from random import randint
num = randint(1, 100)

print('Guess what I think?')
bingo = False

while bingo == False:
    answer = int(input())
    if answer < num:
        print('too small!')

    if answer > num:
        print('too big!')

    if answer == num:
        print('BINGO!')
        bingo = True
