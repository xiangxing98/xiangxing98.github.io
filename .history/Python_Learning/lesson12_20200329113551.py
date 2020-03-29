# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson12.py
@Time    :   2020/03/29 11:35:45
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''

# here put the import lib

from random import randint
num = randint(1, 100)

print('Guess what I think?')
bingo = False
count = 0

while bingo == False:
    count += 1
    answer = int(input())
    if answer < num:
        print('too small! Guess Again')
    if answer > num:
        print('too big! Guess Again')
    if answer == num:
        print('BINGO! Stop Guessing, and Print Guess time Count')
        bingo = True

print(count)
