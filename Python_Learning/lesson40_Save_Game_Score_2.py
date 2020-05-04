# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson40_Save_Game_Score_2.py
@Time    :   2020/05/04 20:11:22
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

# 我们需要有一个变量来记录每次游戏所用的轮数：
times = 0

num = randint(1, 100)
print('Guess what I think?')
bingo = False
while bingo is False:
    answer = int(input())
    bingo = isEqual(answer, num)
    # 然后在游戏每进行一轮的时候，累加游戏所用的轮数这个变量：
    times += 1

# Game Over,当游戏结束后，把这个变量的值，也就是本次游戏的数据，添加到我们的记录中。
# 如果是第一次玩，或者本次的轮数比最小轮数还少，就记录本次成绩为最小轮数：
if game_times == 0 or times < min_times:
    min_times = times

# 把本次轮数加到游戏总轮数里：更新总的游戏轮数
total_times += times

# 把游戏次数加1：
game_times += 1

# 现在有了我们需要的数据，把它们拼成我们需要存储的格式：
result = '%d %d %d' % (game_times, min_times, total_times)

# 写入到文件中：
f = open('game.txt', 'w')
f.write(result)
f.close()

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson40_Save_Game_Score_2.py
'''
