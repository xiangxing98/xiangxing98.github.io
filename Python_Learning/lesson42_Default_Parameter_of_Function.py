# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson42_Default_Parameter_of_Function.py
@Time    :   2020/05/04 21:05:44
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''


# here put the import lib
# 给这个函数一个默认参数
def hello(name='world'):
    print('hello ' + name)


# 调用这个函数：
hello('world2')
# hello world2
hello()
# hello world
hello('python')
# hello python


# 注意，当函数有多个参数时，如果你想给部分参数提供默认参数，那么这些参数必须在参数的末尾。
# def func(a=5, b): SyntaxError: non-default argument follows default argument
def func_test(a, b=5):
    """
    param :
    return:
    """
    print(a, b)


func_test(3, 3)
# 3 3

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson42_Default_Parameter_of_Function.py
'''
