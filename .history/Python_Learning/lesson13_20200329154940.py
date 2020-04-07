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

# print("----\n")
# n = 5

# for i in range(1, n+1):
#     for j in range(0, (n + 1)/2):
#         print("*")
#     for j in range(0, (n + 1)/2):
#         print(" ")
#     print("")

# print("----\n")

# 第1行， 1个*， 四个空格
# 第2行， 一个*， 四个空格
# *
# ***
# *****
# ***
# *

# （1）先打印一个星号并换行
print("-------------------")
print("先打印一个星号并换行\n")
print("*")
print("\n-------------------")

# （2）打印一行6个列星号
print("-------------------")
print("打印一行6个星号\n")
for i in range(6):
    print("*", end=" ")
print("\n-------------------")

#（3）打印6行1列星号
print("-------------------")
print("打印6行1列星号\n")
for i in range(6):
    print("*")
print("\n-------------------")

# （4）打印6行6列
for i in range(6):
    for j in range(6):
        print("*",end=" ")
        # 每打印一行就换行
    print("")
# * * * * * * 
# * * * * * * 
# * * * * * * 
# * * * * * * 
# * * * * * * 
# * * * * * * 


rows = int(input('输入列数：'))
for i in range(1,rows):  
    print('*'*i)








# 打印等腰直角三角形
print("-------------------\n打印等腰直角三角形\n")
for i in range(1, 5):
    for j in range(1, 5):
        if j >= i:
            print("*")
    print("\n")

print("-------------------\n")

# Practice #05
# 输入一个大于等于1的值n，输出星号（*）组成的等腰三角形，底边长为n

# 例：
# 输入
# 3
# 输出
#   *
#  * *
# * * *

print("-------------------\n输出星号（*）组成的等腰三角形，底边长为n\n")
# n = int(input())
n = 8
for i in range(1, n+1):  # n row
    for j in range(0, n-i):  # i row, need n-1 blank
        print(' ', end='')
    for j in range(0, i):  # i row, need i *
        print('*', end='')
    print()  # blank row
print("-------------------------\n")

# -------------------
# 输出星号（*）组成的等腰三角形，底边长为n

# 8
#        *
#       **
#      ***
#     ****
#    *****
#   ******
#  *******
# ********
# -------------------------


# 打印左下角三角形：for i in range(10):之后，range(0,i)
# 打印右上角三角形：在左下角的基础上，将"－"变成" "空格
print("-------------------\n打印左下角三角形\n")
for i in range(10):
    for j in range(0, i):
        print("-", end=" ")

    for j in range(i, 10):
        print("$", end=" ")

    print("")

print("-------------------\n")

# -------------------
# 打印左下角三角形

# $ $ $ $ $ $ $ $ $ $
# - $ $ $ $ $ $ $ $ $
# - - $ $ $ $ $ $ $ $
# - - - $ $ $ $ $ $ $
# - - - - $ $ $ $ $ $
# - - - - - $ $ $ $ $
# - - - - - - $ $ $ $
# - - - - - - - $ $ $
# - - - - - - - - $ $
# - - - - - - - - - $
# -------------------

# 打印左上角三角形：for i in range(10):之后，range(0,10-i)
# 打印右下角三角形：在左上角的基础上，将"－"变成" "空格
print("-------------------\n打印左上角三角形\n")
for i in range(10):
    for j in range(0, 10 - i):
        print("-", end=" ")
    for k in range(10 - i, 10):
        print("$", end=" ")

    print("")
print("-------------------\n")

# -------------------
# 打印左上角三角形

# - - - - - - - - - -
# - - - - - - - - - $
# - - - - - - - - $ $
# - - - - - - - $ $ $
# - - - - - - $ $ $ $
# - - - - - $ $ $ $ $
# - - - - $ $ $ $ $ $
# - - - $ $ $ $ $ $ $
# - - $ $ $ $ $ $ $ $
# - $ $ $ $ $ $ $ $ $
# -------------------

# 打印上三角，只需要将"－",去掉
print("-------------------\n打印上三角\n")
for i in range(10):
    for j in range(0, 10 - i):
        print(end=" ")
    for k in range(10 - i, 10):
        print("$", end=" ")

    print("")
print("-------------------\n")

# -------------------
# 打印上三角

#          $
#         $ $
#        $ $ $
#       $ $ $ $
#      $ $ $ $ $
#     $ $ $ $ $ $
#    $ $ $ $ $ $ $
#   $ $ $ $ $ $ $ $
#  $ $ $ $ $ $ $ $ $
# -------------------

# 打印倒三角，只需要将"－",去掉
print("-------------------\n打印倒三角\n")
for i in range(10):
    for j in range(0, i):
        print(end=" ")

    for j in range(i, 10):
        print("$", end=" ")

    print("")
print("-------------------\n")

# -------------------
# 打印倒三角

# $ $ $ $ $ $ $ $ $ $
#  $ $ $ $ $ $ $ $ $
#   $ $ $ $ $ $ $ $
#    $ $ $ $ $ $ $
#     $ $ $ $ $ $
#      $ $ $ $ $
#       $ $ $ $
#        $ $ $
#         $ $
#          $
# -------------------

# 直角三角形
print("-------------------\n打印直角三角形\n")
# rows = int(input('输入列数：'))
rows = 5
for i in range(1, rows):
    print('*' * i)

for i in range(1, rows):
    for j in range(i):
        print("*", end="")
    print("")
print("-------------------\n")
