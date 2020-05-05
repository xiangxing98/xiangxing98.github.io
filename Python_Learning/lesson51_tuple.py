# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson51_tuple.py
@Time    :   2020/05/05 10:15:01
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''

# here put the import lib
# x, y = pygame.mouse.get_pos()

# 元组（tuple）也是一种序列，和我们用了很多次的list类似，只是元组中的元素在创建之后就不能被修改。

postion = (1, 2)
geeks = ('Sheldon', 'Leonard', 'Rajesh', 'Howard')
# 都是元组的实例。它有和list同样的索引、切片、遍历等操作（参见25～27课）：

print(postion[0])
# 1
for g in geeks:
    print(g)
# Sheldon
# Leonard
# Rajesh
# Howard
print(geeks[1:3])
# ('Leonard', 'Rajesh')

# 其实我们之前一直在用元组，就是在print语句中：
print('%s is %d years old' % ('Mike', 23))
# Mike is 23 years old
# ('Mike', 23)就是一个元组。这是元组最常见的用处。


# 再来看一下元组作为函数返回值的例子：
def get_pos(n):
    return (n/2, n*2)


# 得到这个函数的返回值有两种形式，一种是根据返回值元组中元素的个数提供变量：
x, y = get_pos(50)
print(x)
# 25.0
print("====")
print(y)
# 100
print("====")

# 还有一种方法是用一个变量记录返回的元组：
pos = get_pos(50)
print("====")
print(pos[0])
print(pos[1])

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson51_tuple.py
'''
