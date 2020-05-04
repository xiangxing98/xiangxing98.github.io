# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson36_try_except.py
@Time    :   2020/05/04 18:16:09
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
except OSError:
    print('File not exists.')
print('Python Open File Execute Done!, Pls Check Result.')

# do not use bare except, specify exception instead

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson36_try_except.py
'''
