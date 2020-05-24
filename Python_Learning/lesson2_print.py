# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson2_print.py
@Time    :   2020/05/05 18:29:07
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''

# here put the import lib
# print(你要打印的东西)

print('world')
# world
print(1)
# 1
print(3.14)
# 3.14
print(3e30)
# 3e+30
print(1 + 2 * 3)
# 7
print(2 > 5)
# False

print("Who do you think I am?")
input()
print("Oh, yes!")

# Print 输出
# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：
x = "a"
y = "b"
# 换行输出
print(x)
print(y)

print('---------')
# 不换行输出
print(x, end=" ")
print(y, end=" ")
print()

"""
以上实例执行结果
a
b
---------
a b
"""


'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson2_print.py
'''
