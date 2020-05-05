# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson65_Passing_Arguments_to_Function_1.py
@Time    :   2020/05/05 14:52:21
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''


# here put the import lib
def func(arg1, arg2):
    print(arg1, arg2)


func(3, 7)
# 3 7

func(arg2=3, arg1=7)
# 7 3

# Python 语言还提供了其他一些更灵活的参数传递方式
# func2(a=1, b=2, c=3)
# func3(*args)
# func4(**kargs)


def func(arg1=1, arg2=2, arg3=3):
    print(arg1, arg2, arg3)


# 调用
func(2, 3, 4)
# 2 3 4
func(5, 6)
# 5 6 3
func(7)
# 7 2 3

func(arg2=8)
# 1 8 3

func(arg3=9, arg1=10)
# 10 2 9

func(11, arg3=12)
# 11 2 12

# 但要注意，没有指定参数名的参数必须在所有指定参数名的参数前面，且参数不能重复。
# 以下的调用都是错误的：
# func(arg1=13, 14)
# func(15, arg1=16)

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson65_Passing_Arguments_to_Function_1.py
'''
