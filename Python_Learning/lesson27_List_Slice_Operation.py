# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson27_List_Slice_Operation.py
@Time    :   2020/05/04 10:46:33
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''


# here put the import lib
from random import choice


# lesson27_List_Slice_Operation

# 列表中的元素也可以是别的类型
my_list3 = ['meat', 'egg', 'fish', 'milk', 'tomato', 'potato']

# 不同类型的混合：
my_list4 = [365, 'everyday', 0.618, True]

# 访问 list 中的元素
print(my_list4[1])
# everyday

# 修改list中的元素
print(my_list4[0])
# 365
my_list4[0] = 3651
print(my_list4[0])
# 3651

# 向list中添加元素
print(my_list4)
# [3651, 'everyday', 0.618, True]
my_list4.append(1024)
print(my_list4)
# [3651, 'everyday', 0.618, True, 1024]

# 删除list中的元素
del my_list4[0]
print(my_list4)
# ['everyday', 0.618, True, 1024]

# list还可以处理负数的索引
print("------------------------------------------------------------")
print(my_list4[-1])
print(my_list4[-3])
print("------------------------------------------------------------")
# ------------------------------------------------------------
# 1024
# 0.618
# ------------------------------------------------------------

# 切片操作符是在[]内提供一对可选数字，用:分割。
# 冒号前的数表示切片的开始位置，冒号后的数字表示切片到哪里结束。
# 同样，计数从0开始。
# 注意：开始位置包含在切片中，而结束位置不包括。
# 注意：不管是返回一部分，还是整个列表，都是一个新的对象，与不影响原来的列表。
print("------------------------------------------------------------")
print(my_list4[1:3])
print(my_list4[1:4])
print("------------------------------------------------------------")
# ------------------------------------------------------------
# [0.618, True]
# [0.618, True, 1024]
# ------------------------------------------------------------

# 如果不指定第一个数，切片就从列表第一个元素开始。
# 如果不指定第二个数，就一直到最后一个元素结束。
# 都不指定，则返回整个列表。
# 同索引一样，切片中的数字也可以使用负数。比如：
print("------------------------------------------------------------")
print(my_list4[:3])
print(my_list4[1:])
print(my_list4[:])
print(my_list4[1:-1])
print("------------------------------------------------------------")
# ------------------------------------------------------------
# ['everyday', 0.618, True]
# [0.618, True, 1024]
# ['everyday', 0.618, True, 1024]
# [0.618, True]
# ------------------------------------------------------------

"""
点球小游戏
昨天有了一次罚球的过程，今天我就让它循环5次，并且记录下得分。先不判断胜负。
用score_you表示你的得分，score_com表示电脑得分。开始都为0，每进一球就加1。
"""

print("--罚点球开始--")
score_you = 0
score_com = 0
direction = ['left', 'center', 'right']

for i in range(5):
    print('==== Round %d - You Kick! ====' % (i+1))
    print('Choose one side to shoot:')
    print('left, center, right')
    you = input()
    print('You kicked ' + you)
    com = choice(direction)
    print('Computer saved ' + com)
    if you != com:
        print('Goal!')
        score_you += 1
    else:
        print('Oops...')
    print('Score: %d(you) - %d(com)\n' % (score_you, score_com))

    print('==== Round %d - You Save! ====' % (i+1))
    print('Choose one side to save:')
    print('left, center, right')
    you = input()
    print('You saved ' + you)
    com = choice(direction)
    print('Computer kicked ' + com)
    if you == com:
        print('Saved!')
    else:
        print('Oops...')
        score_com += 1
    print('Score: %d(you) - %d(com)\n' % (score_you, score_com))

print("--罚点球结束--")

# --罚点球开始--
# ==== Round 1 - You Kick! ====
# Choose one side to shoot:
# left, center, right
# left
# You kicked left
# Computer saved right
# Goal!
# Score: 1(you) - 0(com)

# ==== Round 1 - You Save! ====
# Choose one side to save:
# left, center, right
# right
# You saved right
# Computer kicked left
# Oops...
# Score: 1(you) - 1(com)

# ==== Round 2 - You Kick! ====
# Choose one side to shoot:
# left, center, right
# center
# You kicked center
# Computer saved left
# Goal!
# Score: 2(you) - 1(com)

# ==== Round 2 - You Save! ====
# Choose one side to save:
# left, center, right
# right
# You saved right
# Computer kicked center
# Oops...
# Score: 2(you) - 2(com)

# ==== Round 3 - You Kick! ====
# Choose one side to shoot:
# left, center, right
# center
# You kicked center
# Computer saved center
# Oops...
# Score: 2(you) - 2(com)

# ==== Round 3 - You Save! ====
# Choose one side to save:
# left, center, right
# right
# You saved right
# Computer kicked right
# Saved!
# Score: 2(you) - 2(com)

# ==== Round 4 - You Kick! ====
# Choose one side to shoot:
# left, center, right
# center
# You kicked center
# Computer saved right
# Goal!
# Score: 3(you) - 2(com)

# ==== Round 4 - You Save! ====
# Choose one side to save:
# left, center, right
# left
# You saved left
# Computer kicked right
# Oops...
# Score: 3(you) - 3(com)

# ==== Round 5 - You Kick! ====
# Choose one side to shoot:
# left, center, right
# left
# You kicked left
# Computer saved left
# Oops...
# Score: 3(you) - 3(com)

# ==== Round 5 - You Save! ====
# Choose one side to save:
# left, center, right
# left
# You saved left
# Computer kicked left
# Saved!
# Score: 3(you) - 3(com)

# --罚点球结束--
'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson27_List_Slice_Operation.py
'''
