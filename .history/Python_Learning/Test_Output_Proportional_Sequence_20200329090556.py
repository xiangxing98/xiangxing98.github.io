# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   Test_Output_Proportional_Sequence.py
@Time    :   2020/03/29 09:05:39
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''

# here put the import lib

# Proportional sequence output
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

x = 1
sum = 0

while x <= 100:
    sum += x
    x += 1
    print("1 to ", x-1, ", the sum is: " , sum)

print("Final Sum of 1 to 100 is: ", sum)
 
