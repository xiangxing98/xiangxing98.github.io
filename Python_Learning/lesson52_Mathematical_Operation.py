# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson52_Mathematical_Operation.py
@Time    :   2020/05/05 10:29:53
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''

# here put the import lib
# python的数学运算模块叫做math，再用之前，你需要
import math


# math包里有两个常量：
math.pi  # 圆周率π：3.141592...
math.e  # 自然常数：2.718281...

x = 1.2
y = 2
# 数值运算：
math.ceil(x)
# 对x向上取整，比如x=1.2，返回2.0（py3返回2）

math.floor(x)
# 对x向下取整，比如x=1.2，返回1.0（py3返回1）

math.pow(x, y)
# 指数运算，得到x的y次方

math.log(x)
# 对数，默认基底为e。可以使用第二个参数，来改变对数的基底。比如math.log(100, 10)

math.sqrt(x)
# 平方根

math.fabs(x)
# 绝对值

# 三角函数(注意：这里的x是以弧度为单位，所以计算角度的话，需要先换算)
math.sin(x)
math.cos(x)
math.tan(x)
math.asin(x)
math.acos(x)
math.atan(x)

# 角度和弧度互换:
math.degrees(x)
# 弧度转角度

math.radians(x)
# 角度转弧度

# 以上是你平常可能会用到的函数。除此之外，还有一些，这里就不罗列，可以去
# https://docs.python.org/3.7/library/math.html
# 查看官方的完整文档。

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson52_Mathematical_Operation.py
'''
