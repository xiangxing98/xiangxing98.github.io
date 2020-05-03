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

# print('Hello'+1)
# TypeError: can only concatenate str (not "int") to str
# 发生异常: TypeError
# can only concatenate str (not "int") to str
# File "F:\Github\xiangxing98.github.io\Python_Learning\lesson17.py"
# line 28, in <module>
# print('Hello'+1)
print('Hello'+str(1))

# print('hello%d' % '123')
# 发生异常: TypeError
# %d format: a number is required, not str
print("Change String to integer\n")
print('hello%d' % int('123'))
# hello123

# Those statement all true
print(int('123') == 123)
# True
print(float('3.3') == 3.3)
# True
print(str(111) == '111')
# True
print(if(bool(0) == False))

# bool
print("bool \n")
bool(-123)
# True
bool(0)
# False
bool('abc')
# True
bool('False')
# True
bool('')
# False
