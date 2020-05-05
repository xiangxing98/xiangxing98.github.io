# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson61_Debugging_Program.py
@Time    :   2020/05/05 13:24:06
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''


# here put the import lib
import random

"""
import random
a = 0
for i in range(5):
    b = random.choice(range(5))
    a += i / b
print (a)
"""

# 改造之后的
a = 0
for i in range(5):
    print('i: %d' % i)
    b = random.choice(range(5))
    print('b: %d' % b)
    if b == 0:
        print("b equal to 0, skip this cycle and continue\n")
        # break
        continue
    else:
        a += i / b
    print('a: %d' % a)
    print()
print('Finally a: %d' % a)
# Traceback (most recent call last):
#   File "lesson61_Debugging_Program.py", line 22, in <module>
#     a += i / b
# ZeroDivisionError: division by zero

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson61_Debugging_Program.py
'''
