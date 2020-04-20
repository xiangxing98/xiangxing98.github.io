# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson17.py
@Time    :   2020/04/19 21:42:24
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''

# here put the import lib
# 类型转换

a = 1
print(a, type(a))
# 1 <class 'int'>

a = 'hello'
print(a, type(a))
# hello <class 'str'>

a = True
print(a, type(a))
# True <class 'bool'>

print('Hello'+1)
# TypeError: can only concatenate str (not "int") to str

print('hello%d' % '123')
