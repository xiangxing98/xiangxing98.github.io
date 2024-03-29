# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson39_Save_Game_Score_1.py
@Time    :   2020/05/04 19:22:25
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''


# here put the import lib
from random import randint


# 读取文件中的成绩数据
try:
    f = open('game.txt')
    print('File opened!')
    score = f.read().split()
    f.close()
except OSError:
    print('File not exists.')
print('Python Open File Execute Done!, Pls Check Result.')

# 为便于理解，把数据读进来后，分别存在3个变量中。
game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])

# 平均轮数根据总轮数和游戏次数相除得到：
# avg_times = total_times / game_times
# 注意两点：
# 1.python 3的除法运算中，一个"/"的除法，结果为浮点数。
# 如果需要得到结果的整数部分（不是对结果四舍五入），要用"//"，即两个斜杠。
# 而"%"代表对结果取余数。
# 2.因为0是不能作为除数的，所以这里还需要加上判断：
if game_times > 0:
    avg_times = total_times / game_times
else:
    avg_times = 0

# 然后，在让玩家开始猜数字前，输出他之前的成绩信息：
print('你已经玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案' % (
    game_times, min_times, avg_times))
# %.2f这样的写法我们以前也用过，作用是保留两位小数。


def isEqual(num1, num2):
    if num1 < num2:
        print('too small')
        return False
    if num1 > num2:
        print('too big')
        return False
    if num1 == num2:
        print('bingo!')
        return True


# Guess
num = randint(1, 100)
print('Guess what I think?')
bingo = False
while bingo is False:
    answer = int(input())
    bingo = isEqual(answer, num)

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson39_Save_Game_Score_1.py
'''
