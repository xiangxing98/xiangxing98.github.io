# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson7_if.py
@Time    :   2020/03/28 18:58:36
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''

# here put the import lib

# if
# age1 = input()
# age = int(age1)
print('请输入年龄，整数')
age2 = int(input())
if age2 >= 18:
    print("Age > 18, an adult; a grown-up, 你是个成年人了！")
else:
    print('Under 18, teenager')
# 请输入年龄，整数
# 23
# Age > 18, an adult; a grown-up, 你是个成年人了！

# game
num = 10
print('Guess what I think?, Pls Input and integer')
answer = int(input())
if answer < num:
    print('too small!')
if answer > num:
    print('too big!')
if answer == num:
    print('BINGO!')
# Guess what I think?, Pls Input and integer
# 1
# too small!

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson7_if.py
'''
