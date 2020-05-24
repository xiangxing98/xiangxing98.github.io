# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson3_IDE.py
@Time    :   2020/03/28 18:27:57
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''


# here put the import lib
import keyword


# python保留字
# 保留字即关键字，我们不能把它们用作任何标识符名称。
# Python 的标准库提供了一个 keyword 模块，可以输出当前版本的所有关键字：
print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
# 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
# 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
# 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

print("Who do you think I am?")
input()
print("Oh, yes!")

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson3_IDE.py
'''
