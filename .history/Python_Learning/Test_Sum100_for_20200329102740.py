# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   Test_Sum100_for.py
@Time    :   2020/03/29 10:25:34
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''

# here put the import lib

# 输出1+2+3+...+100的和
# 例：
# 5050

x = 1
sum = 0

for x in range(1, 101):
    sum += x
    x += 1
    print("1 to ", x-1, ", the sum is: " , sum)

print("Final Sum of 1 to 100 is: ", sum)
