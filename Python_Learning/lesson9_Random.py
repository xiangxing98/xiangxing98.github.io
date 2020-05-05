# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson9_Random.py
@Time    :   2020/03/28 20:29:00
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''


# here put the import lib
from random import randint


# game-While
# from 模块名 import 方法名
# from random import randint
num = randint(1, 100)

print('Guess what I think?')
bingo = False

while bingo is False:
    print('请输入一个整数，猜猜我是多少？')
    answer = int(input())
    if answer < num:
        print('Tool small, Guess again. %d 太小，再输入一次猜猜看！' % answer)

    if answer > num:
        print('Too big, Guess again.  %d 太大，再输入一次猜猜看！' % answer)

    if answer == num:
        print('BINGO! 太棒， %d 猜对了，退出啦' % answer)
        bingo = True

# Guess what I think?
# 请输入一个整数，猜猜我是多少？
# 50
# Tool small, Guess again. 50 太小，再输入一次猜猜看！
# 请输入一个整数，猜猜我是多少？
# 70
# Tool small, Guess again. 70 太小，再输入一次猜猜看！
# 请输入一个整数，猜猜我是多少？
# 80
# Too big, Guess again.  80 太大，再输入一次猜猜看！
# 请输入一个整数，猜猜我是多少？
# 75
# Tool small, Guess again. 75 太小，再输入一次猜猜看！
# 请输入一个整数，猜猜我是多少？
# 78
# BINGO! 太棒， 78 猜对了，退出啦
# Smith, John

# Recommended Naming Style
name = 'John Smith'
first_name, last_name = name.split()
print(last_name, first_name, sep=', ')
# 'Smith, John'

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson9_Random.py
'''
