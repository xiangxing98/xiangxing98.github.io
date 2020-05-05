# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson66_Passing_Arguments_to_Function_2.py
@Time    :   2020/05/05 15:22:24
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''

# here put the import lib
# 更加灵活的参数传递方式：
# def func(*args)


# 这种方式的厉害之处在于，它可以接受任意数量的参数。来看具体例子：
def calcSum(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)


# 调用：
calcSum(1, 2, 3)
calcSum(123, 456)
calcSum()
# calcSum(range(1, 101))
# 6
# 579
# 0

# 在变量前加上星号前缀（*），调用时的参数会存储在一个 tuple（元组）对象中，赋值给形参。
# 在函数内部，需要对参数进行处理时，
# 只要对这个 tuple 类型的形参（这里是 args）进行操作就可以了。
# 因此，函数在定义时并不需要指明参数个数，就可以处理任意参数个数的情况。


# 不过有一点需要注意，tuple 是有序的，所以 args 中元素的顺序受到赋值时的影响。如：
def printAll(*args):
    for i in args:
        print(i, end=' ')
    print()


# 调用,虽然3个参数在总体上是相同的，但由于调用的顺序不一样，结果也是不同的。
printAll(1, 2, 3)
printAll(3, 2, 1)
# 1 2 3
# 3 2 1

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson66_Passing_Arguments_to_Function_2.py
'''
