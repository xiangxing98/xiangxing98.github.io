# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson71_Reduce_Function.py
@Time    :   2020/05/05 17:47:12
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''


# here put the import lib
from functools import reduce


# 上次说了 Python 中一个比较有意思的内置函数 map，
# 今天再来介绍另一个类似的函数：reduce
# map 可以看作是把一个序列根据某种规则，映射到另一个序列。
# reduce 做的事情就是把一个序列根据某种规则，归纳为一个输出。
# 在 Python3 里，reduce已经被移出内置函数，
# 使用 reduce 需要先通过 from functools import reduce 引入。

# 求1累加到100的和。
# 普通程序员寻常的做法大概是这样：
# from functools import reduce
sum = 0
for i in range(1, 101):
    sum += i
print(sum)

# Pythonic，用 reduce 函数，就可以写成：
lst = range(1, 101)


def add(x, y):
    return x + y


print(reduce(add, lst))
# 5050

# reduce(function, iterable[, initializer])
# 第一个参数是作用在序列上的方法，
# 第二个参数是被作用的序列，这与 map 一致。
# 另外有一个可选参数，是初始值。

# function 需要是一个接收2个参数，并有返回值的函数。
# 它会从序列 iterable 里从左到右依次取出元素，进行计算。
# 每次计算的结果，会作为下次计算的第一个参数。

# 提供初始值 initializer 时，它会作为第一次计算的第一个参数。
# 否则，就先计算序列中的前两个值。
# 如果把刚才的 lst 换成 [1,2,3,4,5]，
# 那 reduce(add, lst) 就相当于 ((((1+2)+3)+4)+5)。

# 同样，可以用 lambda 函数：
# from functools import reduce
reduce((lambda x, y: x + y), range(1, 101))
# 5050

# 所以，在对于一个序列进行某种统计操作的时候，比如求和，
# 或者诸如统计序列中元素的出现个数等（可尝试下如何用 reduce 做到），
# 可以选择使用 reduce 来实现。相对可以使代码更简洁。

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson71_Reduce_Function.py
'''
