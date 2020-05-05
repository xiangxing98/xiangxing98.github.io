# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson22_Function_Apply_Example.py
@Time    :   2020/05/03 18:47:28
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''


# here put the import lib
from random import randint


def isEqual(num1, num2):
    if num1 < num2:
        print('Answer %d too small' % num1)
        return False
    if num1 > num2:
        print('Answer %d too big' % num1)
        return False
    if num1 == num2:
        print('Answer %d bingo!' % num1)
        return True


# Guess
num = randint(1, 100)
print('Guess what I think?')
bingo = False
while bingo is False:
    print('Pls input an integer between 1 and 100')
    answer = int(input())
    bingo = isEqual(answer, num)

# Guess what I think?
# Pls input an integer between 1 and 100
# 50
# Answer 50 too big
# Pls input an integer between 1 and 100
# 25
# Answer 25 too small
# Pls input an integer between 1 and 100
# 35
# Answer 35 too small
# Pls input an integer between 1 and 100
# 45
# Answer 45 too small
# Pls input an integer between 1 and 100
# 47
# Answer 47 too small
# Pls input an integer between 1 and 100
# 48
# Answer 48 bingo!

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson22_Function_Apply_Example.py
'''
