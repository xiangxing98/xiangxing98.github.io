# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson83_Python3_Data_Type.py
@Time    :   2020/05/17 15:51:17
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''

# here put the import lib


counter = 100          # 整型变量
miles = 1000.0       # 浮点型变量
name = "Stone"     # 字符串

print(counter)
print(miles)
print(name)

# 多个变量赋值，创建一个整型对象，值为 1，从后向前赋值，三个变量被赋予相同的数值。
a = b = c = 1

# 两个整型对象 1 和 2 的分配给变量 a 和 b，字符串对象 "Stone" 分配给变量 c。
a, b, c = 1, 2, "Stone"

"""
标准数据类型
Python3 中有六个标准的数据类型：

Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Set（集合）
Dictionary（字典）
Python3 的六个标准数据类型中：

不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
"""

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson83_Python3_Data_Type.py

# Output:
100
1000.0
Stone
'''
