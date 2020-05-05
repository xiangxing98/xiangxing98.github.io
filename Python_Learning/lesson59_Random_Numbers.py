# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson59_Random_Numbers.py
@Time    :   2020/05/05 12:55:31
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''

# here put the import lib
import random
from random import randint

num = random.randint(1, 100)
print(num)

# random.randint(a, b)可以生成一个a到b间的随机整数，包括a和b。
# a、b都必须是整数，且必须b≥a。当等于的时候，比如：
# random.randint(3, 3), 结果就永远是3

# 除了randint，random模块中比较常用的方法还有：
# 生成一个0到1之间的随机浮点数，包括0但不包括1，也就是[0.0, 1.0)。
random.random()
# random.uniform(a, b)

# 生成a、b之间的随机浮点数。不过与randint不同的是，a、b无需是整数，也不用考虑大小。
random.uniform(1.5, 3)
random.uniform(3, 1.5)
# 这两种参数都是可行的

random.uniform(1.5, 1.5)
# 永远得到1.5

# 从序列中随机选取一个元素。seq需要是一个序列，比如list、元组、字符串。
# random.choice(seq)

random.choice([1, 2, 3, 5, 8, 13])  # list
random.choice('hello')  # 字符串
random.choice(['hello', 'world'])  # 字符串组成的list
random.choice((1, 2, 3))  # 元组
# 都是可行的用法。

# 生成一个从start到stop（不包括stop），间隔为step的一个随机数。
# start、stop、step都要为整数，且start<stop。
# 比如：
# random.randrange(start, stop, step)
random.randrange(1, 9, 2)
# 就是从[1, 3, 5, 7]中随机选取一个。
# start和step都可以不提供参数，默认是从0开始，间隔为1。
# 但如果需要指定step，则必须指定start。
random.randrange(4)  # [0, 1, 2, 3]
random.randrange(1, 4)  # [1, 2, 3]

# 下面这两种方式在效果上等同
# random.randrange(start, stop, step)
# random.choice(range(start, stop, step))

# random.sample(population, k)
# 从population序列中，随机获取k个元素，生成一个新序列。sample不改变原来序列。
# random.shuffle(x)
# 把序列x中的元素顺序打乱。shuffle直接改变原有的序列。

# 以上是random中常见的几个方法。如果你在程序中需要其中某一个方法，也可以这样写：
# from random import randint
randint(1, 10)

# 另外，有些编程基础的同学可能知道，在随机数中有个seed的概念，
# 需要一个真实的随机数，比如此刻的时间、鼠标的位置等等，以此为基础产生伪随机数。
# 在python中，默认用系统时间作为seed。你也可以手动调用random.seed(x)来指定seed。

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson59_Random_Numbers.py
'''
