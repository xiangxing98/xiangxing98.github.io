# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson16_String_Format_2.py
@Time    :   2020/04/19 21:35:11
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''

# here put the import lib

# 字符串格式化2
print('%s is easy to learn' % 'python')
# python is easy to learn

print("%s's score is %d" % ('Mike', 87))
# Mike's score is 87

# tuple
name = 'Lily'
score = 95
print("%s's score is %d" % (name, score))
# Lily's score is 95

# ('Mike', 87) 这种用()表示的一组数据在python中被称为元组（tuple），
# 是python的一种基本数据结构，以后我们还会用到。

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson16_String_Format_2.py
'''
