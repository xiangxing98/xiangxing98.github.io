# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson6_bool.py
@Time    :   2020/03/28 18:27:57
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''

# here put the import lib

# bool
a = 1 < 3
print(a)
# True

b = 1
c = 3
print(b > c)
# False

# Game
num = 10
print('Guess what I think?')
# input answer 2
answer = int(input())

result = (answer < num)
print('too small?')
print(result)
# too small?
# True

result = (answer > num)
print('too big?')
print(result)
# too big?
# False

result = (answer == num)
print('equal?')
print(result)
# equal?
# False

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson6_bool.py
'''
