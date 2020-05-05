# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson8_While.py
@Time    :   2020/03/28 19:47:28
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''

# here put the import lib

# while
a = 1             # 为了后面的条件能满足，先把a设为1
while a != 0:     # 如果a不等于0就循环（1不等于0）
    print("please input a number between -10 to 10")
    a = int(input())     # 在循环内部获取输入，改变a的值（想想看不改会怎样？）
print("over")
# please input a number between -10 to 10
# 3
# please input a number between -10 to 10
# 0
# over

# game-While
num = 10
print('Guess what I think?')
bingo = False

while bingo is False:
    print('请输入一个整数，猜猜我是多少？')
    answer = int(input())
    if answer < num:
        print('Tool small, Guess again. 太小，再输入一次猜猜看！')

    if answer > num:
        print('Too big, Guess again. 太大，再输入一次猜猜看！')

    if answer == num:
        print('BINGO! 太棒，猜对了，退出啦')
        bingo = True

# Guess what I think?
# 请输入一个整数，猜猜我是多少？
# 5
# Tool small, Guess again. 太小，再输入一次猜猜看！
# 请输入一个整数，猜猜我是多少？
# 15
# Too big, Guess again. 太大，再输入一次猜猜看！
# 请输入一个整数，猜猜我是多少？
# 10
# BINGO! 太棒，猜对了，退出啦

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson8_While.py
'''
