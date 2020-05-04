# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson34_break.py
@Time    :   2020/05/04 17:51:25
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''


# here put the import lib

while True:
    a = input()
    if a == 'EOF':
        print("Exit")
        break

for i in range(10):
    a = input()
    if a == 'EOF':
        print("Exit")
        break

for i in range(5):
    answer = input()
    if answer < 0:
        print('Exit game...')
        break

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson34_break.py
'''
