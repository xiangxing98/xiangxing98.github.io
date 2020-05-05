# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson12_for_loop.py
@Time    :   2020/03/29 11:35:45
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''

# here put the import lib
# for 循环本质是对一个序列中的元素进行遍历。for i in range(a, b) 从 a 循环至 b-1

# for ... in ...输出1到100
for i in range(1, 101):
    print(i)
# 1
# 2
# ...
# 99
# 100

# equal to below
for i in range(0, 100):
    print(i)
# 1
# 2
# ...
# 99
# 100

# 当你需要一个循环10次的循环，你就只需要写：
for i in range(1, 11):
    print(i)
# 1
# 2
# ...
# 9
# 10

# equal to
for i in range(0, 10):
    print(i)
# 0
# 1
# 2
# ...
# 8
# 9

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson12_for_loop.py
'''
