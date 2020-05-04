# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson41_Save_Game_Score_3.py
@Time    :   2020/05/04 20:20:05
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''


# here put the import lib
from random import randint


# 存储多组成绩。
# 首先要输入名字，这是我们用来区分玩家成绩的依据：
name = input('请输入你的名字：')

# 读取文件中的成绩数据
# 接下来，我们读取文件。与之前不同，我们用readlines把每组成绩分开来：
try:
    f = open('game_score.txt')
    print('File opened!')
    lines = f.readlines()
    f.close()
except OSError:
    print('File not exists.')
print('Python Open File Execute Done!, Pls Check Result.')

# 再用一个字典来记录所有的成绩，先初始化一个空字典
scores = {}
for l in lines:
    s = l.split()              # 把每一行的数据拆分成List
    scores[s[0]] = s[1:]       # 第一项作为key, 剩下的作为value

# scores这个字典中，每一项的key是玩家的名字，value是一个由剩下的数据组成的数组。
# 这里每一个value就相当于我们之前的成绩数据。
# 我们要找到当前玩家的数据：
# 字典类的get方法是按照给定key寻找对应项，如果不存在这样的key，就返回空值None。
score = scores.get(name)

# 如果没有找到该玩家的数据，说明他是一个新玩家，我们给他初始化一组成绩：
if score is None:
    score = [0, 0, 0]

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

# 然后，在让玩家开始猜数字前，输出他之前的成绩信息， 加上显示玩家的名字
print('%s, 你已经玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案' % (
    name, game_times, min_times, avg_times))
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


# Guess what i input

# 我们需要有一个变量来记录本次游戏所用的轮数：
times = 0

num = randint(1, 100)
print('Guess what I think?')
bingo = False
while bingo is False:
    answer = int(input())
    bingo = isEqual(answer, num)
    # 然后在游戏每进行一轮的时候，累加游戏所用的轮数这个变量：
    times += 1

# Game Over,游戏结束后，把这个变量的值，也就是本次游戏的数据，添加到我们的记录中。
# 如果是第一次玩，或者本次的轮数比最小轮数还少，就记录本次成绩为最小轮数：
if game_times == 0 or times < min_times:
    min_times = times

# 把本次轮数加到游戏总轮数里：更新总的游戏轮数
total_times += times

# 把游戏次数加1：
game_times += 1

# 当游戏结束，记录成绩的时候，和之前的方法不一样。
# 我们不能直接把这次成绩存到文件里，那样就会覆盖掉别人的成绩。

# 必须先把成绩更新到scores字典中，再统一写回文件中。
# 把成绩更新到对应的玩家scores中，加str转换成字符串，为后面的格式化准备
# 如果没有这一项，会自动生成新条目：
scores[name] = [str(game_times), str(min_times), str(total_times)]

# 对于每一项成绩，我们要将其格式化：
result = ''  # 初始化一个空字符串，用来存储数据
for n in scores:
    # 把数据按照"name game_times min_time total_times" 格式化
    # 把scores中的每一项按照“名字 游戏次数 最低轮数 总轮数\n”的格式拼成字符串，
    # 结尾要加上\n换行
    line = n + ' ' + ' '.join(scores[n]) + '\n'
    result += line  # 再全部添加到result里，就得到了我们要保存的结果。

# 写入到文件中：
f = open('game_score.txt', 'w', encoding='utf-8')
f.write(result)
f.close()

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson41_Save_Game_Score_3.py
'''
