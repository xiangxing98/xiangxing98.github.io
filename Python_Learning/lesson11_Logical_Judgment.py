# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson11_Logical_Judgment.py
@Time    :   2020/03/29 11:38:24
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''

# here put the import lib

print(1 < 3)
# True

print(2 == 3)
# False

print('=====Start=====')
a = 1
print(a > 3)
print(a == 2-1)
b = 3
print(a+b == 2+2)
print('=====End=====')
# =====Start=====
# False
# True
# True
# =====End=====

a = False
print(a)
# False
print(a is False)
# True

# 把bingo设为一个值为False的变量
bingo = False

# 判断bingo的值是不是False，如果是，那么这句话就是True
print(bingo is False)
# True

# Exercise
a = True
b = not a  # 不记得not请回顾 6.bool

print(b)
# False

print(not b)
# True

print(a == b)
# False

print(a != b)
# True

print(a and b)
# False

print(a or b)
# True

print(1 < 2 and b is True)
# False

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson11_Logical_Judgment.py
'''
