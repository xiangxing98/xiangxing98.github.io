# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson29_Join_List.py
@Time    :   2020/05/04 12:58:20
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''


# here put the import lib

sting_to_join = ';'
list_apple = ['apple', 'pear', 'orange']
fruit = sting_to_join.join(list_apple)
print(fruit)
# apple;pear;orange

join_str1 = ';'.join(['apple', 'pear', 'orange'])
join_str2 = ''.join(['hello', 'world'])
print("--Start--")
print(join_str1)
print(join_str2)
print("--End--")
# --Start--
# apple;pear;orange
# helloworld
# --End--

# import os
# os.system("ipconfig")

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson29_Join_List.py
'''
