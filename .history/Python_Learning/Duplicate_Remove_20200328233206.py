# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   random.py
@Time    :   2020/03/28 20:50:56
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''

# 今天的坑： 从一组数据中去除掉重复的元素，并将其排序输出。
# 比如：
# 4, 7, 3, 4, 1, 9, 8, 3, 7
# 输出结果：
# 1, 3, 4, 7, 8, 9

li = [4, 7, 3, 4, 1, 9, 8, 3, 7]
sorted(set(li))
