# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson10_variable_2.py
@Time    :   2020/03/28 20:50:56
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''


# here put the import lib
from random import randint

# variable_2
# 变量名不是你想起就能起的：

# 第一个字符必须是字母或者下划线_
# 剩下的部分可以是字母、下划线_或数字0~9
# 变量名称是对大小写敏感的，my_name 和 my_Name 不是同一个变量。

# 几个有效的栗子：
# i
# __my_name
# name_23
# a1b2_c3

# 几个坏掉的栗子
# 2things
# this is spaced out
# my-name

# 变量的运算

# 存储数据
num = 10
answer = int(input())

# 比较大小
answer < num

# 进行数学运算
a = 5
b = a + 3
c = a + b
a = a + 3
print(a)
# 8

# a = a + 3 same as a += 3
a += 3
print(a, "\n")
# 11

# Guess Number Game again
# from random import randint
print('Guess what I think?')
num = randint(1, 100)  # 随机数字初始化
bingo = False  # 是否猜中初始化
count = 0  # 轮次初始化

while bingo is False:
    # 开始计数，猜了几轮
    count += 1
    print('请输入一个整数，猜猜我是多少？')
    answer = int(input())
    if answer < num:
        print('Tool small, Guess again. %d 太小，再输入一次猜猜看！' % answer)

    if answer > num:
        print('Too big, Guess again.  %d 太大，再输入一次猜猜看！' % answer)

    if answer == num:
        print('BINGO! 太棒， %d 猜对了，退出啦' % answer)
        bingo = True

print("你总共猜了 ", count, " 轮次后猜中了，恭喜你！")

# Guess what I think?
# 请输入一个整数，猜猜我是多少？
# 30
# Too big, Guess again.  30 太大，再输入一次猜猜看！
# 请输入一个整数，猜猜我是多少？
# 20
# Tool small, Guess again. 20 太小，再输入一次猜猜看！
# 请输入一个整数，猜猜我是多少？
# 25
# Tool small, Guess again. 25 太小，再输入一次猜猜看！
# 请输入一个整数，猜猜我是多少？
# 29
# Too big, Guess again.  29 太大，再输入一次猜猜看！
# 请输入一个整数，猜猜我是多少？
# 26
# BINGO! 太棒， 26 猜对了，退出啦
# 你总共猜了  5  轮次后猜中了，恭喜你！

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson10_variable_2.py
'''
