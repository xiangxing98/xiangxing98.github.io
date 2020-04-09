# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson15.py
@Time    :   2020/04/07 23:35:14
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''

# here put the import lib

# 输出5个 *, 分5行
print("\n输出5个 *, 分5行\n")
for i in range(0, 5):
    print('*')

# 让这5个*在同一行，需要加上 end 参数，使得 print 之后不换行
# end 参数的作用是指定 print 结束之后的字符，默认是回车。你可以试试设置成不同字符的效果。
print("\n输出5个 *, 在同一行\n")
for i in range(0, 5):
    print('*', end='')

# 让这5个*在同一行，5行需要加上 end 参数，使得 print 之后不换行
print("\n输出25个 *, 在同一行\n")
for i in range(0, 5):
    print('*****', end='')

print("\n输出5个 *, 在同一行，输出5行\n")
for i in range(0, 5):
    print('*****')
# *****
# *****
# *****
# *****
# *****

# 两个嵌套在一起的循环：
for i in range(0, 3):
    for j in range(0, 3):
        print(i, j)
# 0 0
# 0 1
# 0 2
# 1 0
# 1 1
# 1 2
# 2 0
# 2 1
# 2 2   

#  5*5
for i in range(0, 5):
    for j in range(0, 5):
        print('*', end='\t')
    print()
# print 的括号里没有写任何东西，是起到换行的作用，这样，每输出5个*，就会换行。

for i in range(0, 5):
    for j in range(0, i+1):
        print('*', end='-')
    print()
# *-
# *-*-
# *-*-*-
# *-*-*-*-
# *-*-*-*-*-

print("---\n")

for i in range(0, 5):
    for j in range(0, i+1):
        print(' ')
        #print('*', end='-')
    print('*', end='-')
print()
