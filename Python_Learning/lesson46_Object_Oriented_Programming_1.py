# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson46_Object_Oriented_Programming_1.py
@Time    :   2020/05/04 22:11:55
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''


# here put the import lib

my_string = 'how are you'
# s被赋值后就是一个字符串类型的对象
my_list = my_string.split()
# split是字符串的方法，这个方法返回一个list类型的对象
# my_list是一个list类型的对象

# 通过dir()方法可以查看一个类/变量的所有属性：
print(dir(my_string), '\n')
print(dir(my_list))

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson46_Object_Oriented_Programming_1.py
'''
