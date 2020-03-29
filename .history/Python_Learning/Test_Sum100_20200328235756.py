# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   Test_Sum100.py
@Time    :   2020/03/28 23:56:07
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

while x <= 100:
    sum += x
    x += 1
    print("Temp Sum is: ")

print("Final Sum of 1 to 100 is: ", sum)
