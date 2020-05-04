# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson26_List_Operation.py
@Time    :   2020/05/04 10:40:47
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''


# here put the import lib
from random import choice
# lesson26_List_Operation


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

"""
我打算从今天开始，每天说一点这个小游戏的做法。
方法有很多种，我只是提供一种参考。你可以按照自己喜欢的方式去做，那样她才是属于你的游戏。

先说一下方向的设定。我的想法比较简单，就是左、中、右三个方向，用字符串来表示。
射门或者扑救的时候，直接输入方向。所以这里我准备用 input。
有同学是用1-9的数字来表示八个方向和原地不动，每次输入一个数字，这也是可以的。
不过这样守门员要扑住的概率可就小多了。

至于电脑随机挑选方向，如果你是用数字表示，就用我们之前讲过的randint来随机就行。
不过我这次打算用random的另一个方法：choice。它的作用是从一个list中随机挑选一个元素。

于是，罚球的过程可以这样写：
"""

print('Choose one side to shoot:')
print('left, center, right')
you = input()
print('You kicked ' + you)
direction = ['left', 'center', 'right']
com = choice(direction)
print('Computer saved ' + com)
if you != com:
    print('Goal!')
else:
    print('Oops...')

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson26_List_Operation.py
'''
