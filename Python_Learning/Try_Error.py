# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   Try_Error.py
@Time    :   2020/04/11 23:00:24
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''

# here put the import lib
try:
    f = open('non-exist.txt')
    print('File opened!')
    f.close()
except IOError:
    print('File not exists.')
print('Done')
