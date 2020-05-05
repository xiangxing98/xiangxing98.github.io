# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson68_Lambda_Expression.py
@Time    :   2020/05/05 16:18:13
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''


# here put the import lib
# lambda 表达可以被看做是一种匿名函数。
# 它可以让你快速定义一个极度简单的单行函数。譬如这样一个实现三个数相加的函数：
def sum(a, b, c):
    return a + b + c


print(sum(1, 2, 3))
# 6
print(sum(4, 5, 6))
# 15


# 如果使用 lambda 表达式来实现：
def sum(a, b, c): return a + b + c


print(sum(1, 2, 3))
print(sum(4, 5, 6))


# 把 lambda 表达式用在 def 函数定义中
def fn(x):
    return lambda y: x + y


a = fn(2)
print(a(3))

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson68_Lambda_Expression.py
'''
