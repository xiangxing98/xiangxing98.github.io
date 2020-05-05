# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson70_Map_Function.py
@Time    :   2020/05/05 17:29:57
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''

# here put the import lib

# 来看两个问题：
# 1. 假设有一个数列，如何把其中每一个元素都翻倍？
# 2. 假设有两个数列，如何求和？

# 普通程序员
lst_1 = [1, 2, 3, 4, 5, 6]
lst_2 = []
for item in lst_1:
    lst_2.append(item * 2)
print(lst_2)
# [2, 4, 6, 8, 10, 12]

# Python 程序员大概会这么写：
lst_1 = [1, 2, 3, 4, 5, 6]
lst_2 = [i * 2 for i in lst_1]
print(lst_2)
# [2, 4, 6, 8, 10, 12]

# 另一种 Python 程序员常用的写法 -- map：
lst_1 = [1, 2, 3, 4, 5, 6]


def double_func(x):
    return x * 2


lst_2 = map(double_func, lst_1)
print(list(lst_2))
# [2, 4, 6, 8, 10, 12]
# 在py3里必须将lst_2转换成list对象后输出

# map 是 Python 自带的内置函数，它的作用是把一个函数应用在一个（或多个）序列上，
# 把列表中的每一项作为函数输入进行计算，再把计算的结果以列表的形式返回。
# map 的第一个参数是一个函数，之后的参数是序列，可以是 list、tuple。

# 刚刚那个问题也可以写成lambda函数：
# 这里原数据改为了元组，函数用 lambda 表达式替代。
lst_1 = (1, 2, 3, 4, 5, 6)
lst_2 = map(lambda x: x * 2, lst_1)
print(list(lst_2))

# map 中的函数可以对多个序列进行操作。
# 最开始提出的第二个问题，除了通常的 for 循环写法，
# 如果用列表综合的方法比较难实现，但用 map 就比较方便：
lst_1 = [1, 2, 3, 4, 5, 6]
lst_2 = [1, 3, 5, 7, 9, 11]
lst_3 = map(lambda x, y: x + y, lst_1, lst_2)
print(list(lst_3))
# [2, 5, 8, 11, 14, 17]

# map 中的函数会从对应的列表中依次取出元素，作为参数使用，同样将结果以列表的形式返回。
# 所以要注意的是，函数的参数个数要与 map 中提供的序列组数相同，
# 即函数有几个参数，就得有几组数据。
# 对于每组数据中的元素个数，如果有某组数据少于其他组，map 会以 None 来补全这组参数。

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson70_Map_Function.py
'''
