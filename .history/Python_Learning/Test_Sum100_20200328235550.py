# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   Duplicate_Remove.py
@Time    :   2020/03/28 23:32:15
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''

# here put the import lib

# 今天的坑： 从一组数据中去除掉重复的元素，并将其排序输出。
# 比如：
# 4, 7, 3, 4, 1, 9, 8, 3, 7
# 输出结果：
# 1, 3, 4, 7, 8, 9

li = [4, 7, 3, 4, 1, 9, 8, 3, 7]
li2 = sorted(set(li))
print(li2)
# [1, 3, 4, 7, 8, 9]

x = 1

sum = 0

while x <= 100:

  sum += x

  x += 1

print(sum)

