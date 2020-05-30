# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson5_Variable_Data_Type.py
@Time    :   2020/05/24 23:27:54
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''

# here put the import lib


counter = 100       # 整型变量
miles = 1000.0      # 浮点型变量
name = "Stone_Hou"     # 字符串

print(counter)
print(miles)
print(name)
# 100
# 1000.0
# Stone_Hou

# Var
name = 'Crossin'
myVar = 123
price = 5.99
visible = True

print(name)
# Crossin

a = 123
print(a)
# 123

a = 'hi'
print(a)
# hi

value = 3 * 4
print(value)
# 12

value = 2 < 5
print(value)
# True

name = input()
print(name)
# haha
# haha

# improve game
print("Who do you think I am?")
you = input()
print("Oh, yes! I am a")
print(you)
# Who do you think I am?
# haha
# Oh, yes! I am a
# haha

# 多个变量赋值, 创建一个整型对象，值为 1，从后向前赋值，三个变量被赋予相同的数值。
a = b = c = 1

# 您也可以为多个对象指定多个变量。例如：
a, b, c = 1, 2, "Stone_Hou"
# 两个整型对象 1 和 2 的分配给变量 a 和 b，字符串对象 "Stone_Hou" 分配给变量 c。

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

Number（数字）
Python3 支持 int、float、bool、complex（复数）。

在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。

像大多数语言一样，数值类型的赋值和计算都是很直观的。

内置的 type() 函数可以用来查询变量所指的对象类型。

"""

# 数值数字：数字数据类型用于存储数值，不可改变的数据类型
var1 = 1
var2 = 10

# 使用del语句删除一些对象的引用。
# del var1[,var2[,var3[....,varN]]]]
# del var1
del var1, var2

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson5_Variable_Data_Type.py

# Output:

'''
