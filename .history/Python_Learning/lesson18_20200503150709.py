# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson18.py
@Time    :   2020/05/03 14:55:35
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''

# here put the import lib
print(bool('False'))
# True

a = '123'
if a:
    print('1.this is not a blank string')

# equals to
a = '123'
if bool(a) == True:
    print('2. this is not a blank string')

# equals to
a = '123'
if a != '':
    print('3. this is not a blank string')
