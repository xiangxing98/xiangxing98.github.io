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
for i in range(0, 5):
    print('*')

# 让这5个*在同一行，需要加上 end 参数，使得 print 之后不换行
# end 参数的作用是指定 print 结束之后的字符，默认是回车。你可以试试设置成不同字符的效果。
for i in range(0, 5):
    print('*', end='')

for i in range(0, 5):
    print('*****', end='')
