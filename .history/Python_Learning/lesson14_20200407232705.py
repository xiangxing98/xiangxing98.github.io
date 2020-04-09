# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson14.py
@Time    :   2020/04/07 22:48:46
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''

# here put the import lib

str1 = 'good'
str2 = 'bye'

print(str1 + str2)

print('very' + str1)

print(str1 + ' and ' + str2)

num = 18
# print('My age is' + num)
# 发生异常: TypeError
# can only concatenate str (not "int") to str

print('My age is' + str(num))

# 用 % 对字符串进行格式化,原始字符串中的 %d 会被 % 后面的值替换
print('My age is %d' % num)

# %d 只能用来替换整数。如果你想格式化的数值是小数，要用 %f
print('Price is %f' % 4.99)

# 如果你想保留两位小数，需要在f前面加上条件：%.2f
print('Price is %.2f' % 4.99)

# Practice

from random import randint
num = randint(1, 100)

print('Guess what I think?')
bingo = False
count = 0

while bingo == False:
    count += 1
    answer = int(input())
    if answer < num:
        print(str(answer) + ' is too small! Guess Again')
    if answer > num:
        print(str(answer) + ' is too big! Guess Again')
    if answer == num:
        print('BINGO! ' + str(answer) + ' is the Right Answer,  
        Stop Guessing, and Print Guess time Count')
        bingo = True

print('Your Guessing Count is %d' % count)
