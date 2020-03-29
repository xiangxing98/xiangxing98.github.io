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
# 输入一个大于等于3的值n，输出斐波纳契数列的前n项。
# 注：斐波纳契数列：1,1,2,3,5,8,13,21...前两项为1，从第3项起，每一项是前两项的和

# 例：
# 输入
# 7
# 输出
# 1
# 1
# 2
# 3
# 5
# 8
# 13

print("Pls input Fibonacci Series number")

n = float(input())
x = 3
a1 = 1
a2 = 1
print(a1)
print(a2)

while x <= n:
    a3 = a1 + a2
    print(a3)
    a1 = a2
    a2 = a3
    x += 1
