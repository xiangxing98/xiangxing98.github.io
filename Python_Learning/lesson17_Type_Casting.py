# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson17_Type_Casting.py
@Time    :   2020/04/19 21:42:24
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''

# here put the import lib
# 类型转换 Type_Casting

# 变量 a 先后成为了整数int、字符串str、bool类型。
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

# python提供了一些方法对数值进行类型转换：
# int(x)     #把x转换成整数
# float(x)  #把x转换成浮点数
# str(x)     #把x转换成字符串
# bool(x)   #把x转换成bool值

print('Hello'+str(1))
# Hello1

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

print('=====Start=====')
# =====Start=====

# bool
print("----bool----")
# ----bool----

# bool(0) == False
print(bool(0) is False)
# True

print(bool(-123))
# True

print(bool(0))
# False

print(bool('abc'))
# True

print(bool('False'))
# True

print(bool(''))
# False

print(bool(' '))
# True

print('=====End=====')
# =====End=====

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson17_Type_Casting.py
'''
