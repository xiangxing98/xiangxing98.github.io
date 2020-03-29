# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   Test_Output_Fibonacci_Series.py
@Time    :   2020/03/29 09:26:04
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''

# here put the import lib


# Test_Output_Fibonacci_Series
# 输入一个值，输出以这个值为公比，1为首项的等比数列前10项
# 例：
# 输入
# 2
# 输出
# 1
# 2
# 4
# 8
# 16
# 32
# 64
# 128
# 256
# 512

print("Pls input Proportional number")

q = int(input())
n = 1
an = 1

while n <= 10:
    print(an)
    an *= q
    n += 1
