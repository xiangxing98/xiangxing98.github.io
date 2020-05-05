# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson50_and_or.py
@Time    :   2020/05/05 09:25:49
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''

# here put the import lib

a = "heaven"
b = "hell"
c = True and a or b
print(c)
# heaven
# 结果很奇怪是不是？
# 表达式从左往右运算，1和"heaven"做and的结果是"heaven"，
# 再与"hell"做or的结果是"heaven"；
d = False and a or b
print(d)
# hell
# 0和"heaven"做and的结果是0，再与"hell"做or的结果是"hell"。

# 抛开绕人的and和or的逻辑，你只需记住，在一个bool and a or b语句中，
# 当bool条件为真时，结果是a；当bool条件为假时，结果是b。
# 有学过c/c++的同学应该会发现，这和bool?a:b表达式很像。

# 有了它，原本需要一个if-else语句表述的逻辑：
a = -2
if a > 0:
    print("big")
else:
    print("small")

# 就可以直接写成：
print((a > 0) and "big" or "small")

# 然而不幸的是，如果直接这么用，有一天你会踩到坑的。
# 和c语言中的?:表达式不同，这里的and or语句是利用了python中的逻辑运算实现的。
# 当a本身是个假值（如0，""）时，结果就不会像你期望的那样。

a = ""
b = "hell"
c = True and a or b
print(c)
# hell
# 得到的结果不是""而是"hell"。因为""和"hell"做or的结果是"hell"。

# 所以，and-or真正的技巧在于，确保a的值不会为假。
# 最常用的方式是使 a 成为 [a] 、 b 成为 [b]，然后使用返回值列表的第一个元素：
a = ""
b = "hell"
c = (True and [a] or [b])[0]
print(c)
# 由于[a]是一个非空列表，所以它决不会为假。
即使a是0或者''或者其它假值，列表[a]也为真，因为它有一个元素。

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson50_and_or.py
'''
