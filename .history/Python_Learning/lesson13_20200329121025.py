# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson13.py
@Time    :   2020/03/29 11:43:27
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''

# here put the import lib

# Practice #01
print('He said,"I\'m yours!"')
# He said, "I'm yours!"

# Practice #02
print('\\\\_v_//')
# \\_v_//

# Practice #03
print("Stay hungry, \n\
stay foolish.\n\
             -- Steve Jobs")
# Stay hungry,
# stay foolish.
#              -- Steve Jobs

# Practice #04
n = 5

for i in range(1, n+1):
    for j in range(0, i):
        print("*")
    for j in range(0, n-i):
        print("*")
    print("*")


# *
# ***
# *****
# ***
# *

# Practice #05
# 输入一个大于等于1的值n，输出星号（*）组成的等腰三角形，底边长为n

# 例：
# 输入
# 3
# 输出
#   *
#  * *
# * * *

n = input()
for i in range(1, n+1): # n row
   for j in range(0, n-i): # i row, need n-1 blank
      print(' ',end='')
   for j in range(0, i): # i row, need i *
      print('*',end='')
   print() # blank row