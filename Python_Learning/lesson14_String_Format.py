# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson14_String_Format.py
@Time    :   2020/04/07 22:48:46
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''


# here put the import lib
from random import randint


str1 = 'good'
str2 = 'bye'

print(str1 + str2)
# goodbye

print('very' + str1)
# verygood

print(str1 + ' and ' + str2)
# good and bye

# 字符和数字不能直接用 + 相加
# 如果你想要把一个数字加到文字后面输出，程序就会报错
num = 18
# print('My age is' + num)
# 发生异常: TypeError
# can only concatenate str (not "int") to str

# 解决办法，用str()把数字转换成字符串
print('My age is ' + str(num))
# My age is 18

# 用 % 对字符串进行格式化,原始字符串中的 %d 会被 % 后面的值替换
print('My age is %d' % num)
# My age is 18

# %d 只能用来替换整数。如果你想格式化的数值是小数，要用 %f
print('Price is %f' % 4.99)

# 如果你想保留两位小数，需要在f前面加上条件：%.2f
print('Price is %.2f' % 4.99)
# Price is 4.990000

# 用 %s 来替换一段字符串
name = 'Stone_Hou'
print('%s is a good teacher.' % name)
# Stone_Hou is a good teacher.

print('Today is %s.' % 'Friday')
# Today is Friday

# Practice

# from random import randint
num = randint(1, 100)

print('Guess what I think?')
bingo = False
count = 0

while bingo is False:
    count += 1
    print('Pls input and integer between 1 and 100: ')
    answer = int(input())
    if answer < num:
        print(str(answer) + ' is too small! Guess Again')
    if answer > num:
        print(str(answer) + ' is too big! Guess Again')
    if answer == num:
        print('BINGO! ' + str(answer) + ' is the Right Answer.')
        bingo = True

print('Your Guessing Count is %d' % count)

# Guess what I think?
# Pls input and integer between 1 and 100:
# 1
# 1 is too small! Guess Again
# Pls input and integer between 1 and 100:
# 90
# 90 is too big! Guess Again
# Pls input and integer between 1 and 100:
# 45
# 45 is too big! Guess Again
# Pls input and integer between 1 and 100:
# 30
# 30 is too big! Guess Again
# Pls input and integer between 1 and 100:
# 20
# 20 is too big! Guess Again
# Pls input and integer between 1 and 100:
# 15
# 15 is too big! Guess Again
# Pls input and integer between 1 and 100:
# 10
# 10 is too small! Guess Again
# Pls input and integer between 1 and 100:
# 13
# 13 is too small! Guess Again
# Pls input and integer between 1 and 100:
# 14
# BINGO! 14 is the Right Answer.
# Your Guessing Count is 9

# 1.针对字符串的测试
condition1 = ''
if condition1:
    print('condition1 True')
else:
    print('condition1 False')
# False

condition2 = 'test'
if condition2:
    print('condition2 True')
else:
    print('condition2 False')
# True

# 2.针对原组的测试
condition3 = ()
if condition3:
    print('condition3 True')
else:
    print('condition3 False')
# False

condition4 = (1, 2)
if condition4:
    print('condition4 True')
else:
    print('condition4 False')
# True

# 3.针对列表的测试
condition5 = []
if condition5:
    print('condition5 True')
else:
    print('condition5 False')
# False

condition6 = ['a', 'b']
if condition6:
    print('condition6 True')
else:
    print('condition6 False')
# True

# 4.针对字典的测试
condition7 = {}
if condition7:
    print('condition7 True')
else:
    print('condition7 False')
# False
condition8 = {'k': 'v'}
if condition8:
    print('condition8 True')
else:
    print('condition8 False')
# True

# 5.针对None的测试
condition9 = None
if condition9:
    print('condition9 True')
else:
    print('condition9 False')
# False

# 6.针对set()的测试
condition10 = set()
if condition10:
    print('condition10 True')
else:
    print('condition10 False')
# False

condition11 = condition10.add('a')
if condition11:
    print('condition11 True')
else:
    print('condition11 False')
# True

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson14_String_Format.py
'''
