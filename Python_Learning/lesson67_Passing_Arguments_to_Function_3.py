# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson67_Passing_Arguments_to_Function_3.py
@Time    :   2020/05/05 15:36:18
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''

# here put the import lib
# 最为灵活的一种参数传递方式：
# 上次说的 func(*args) 方式是把参数作为 tuple 传入函数内部。
# 而 func(**kargs) 则是把参数以键值对字典的形式传入。


def printAll(**kargs):
    for k in kargs:
        print(k, ':', kargs[k])


printAll(a=1, b=2, c=3)
printAll(x=4, y=5)
# a : 1
# b : 2
# c : 3
# x : 4
# y : 5

# 字典是无序的，所以在输出的时候，并不一定按照提供参数的顺序。同样在调用时，
# 参数的顺序无所谓，只要对应合适的形参名就可以了。
# 于是，采用这种参数传递的方法，可以不受参数数量、位置的限制。


# 混合使用函数调用
def func(x, y=5, *a, **b):
    print(x, y, a, b)


func(1)
# 1 5 () {}
func(1, 2)
# 1 2 () {}
func(1, 2, 3)
# 1 2 (3,) {}
func(1, 2, 3, 4)
# 1 2 (3, 4) {}
func(x=1)
# 1 5 () {}
func(x=1, y=1)
# 1 1 () {}
func(x=1, y=1, a=1)
# 1 1 () {'a': 1}
func(x=1, y=1, a=1, b=1)
# 1 1 () {'a': 1, 'b': 1}
func(1, y=1)
# 1 1 () {}
func(1, 2, 3, 4, a=1)
# 1 2 (3, 4) {'a': 1}
func(1, 2, 3, 4, k=1, t=2, o=3)
# 1 2 (3, 4) {'k': 1, 't': 2, 'o': 3}

# 在混合使用时，首先要注意函数的写法，必须遵守：
# 带有默认值的形参(arg=)须在无默认值的形参(arg)之后；
# 元组参数(*args)须在带有默认值的形参(arg=)之后；
# 字典参数(**kargs)须在元组参数(*args)之后。

# 可以省略某种类型的参数，但仍需保证此顺序规则。

# 调用时也需要遵守：

# 指定参数名称的参数要在无指定参数名称的参数之后；
# 不可以重复传递，即按顺序提供某参数之后，又指定名称传递。

# 而在函数被调用时，参数的传递过程为：

# 按顺序把无指定参数的实参赋值给形参；
# 把指定参数名称(arg=v)的实参赋值给对应的形参；
# 将多余的无指定参数的实参打包成一个 tuple 传递给元组参数(*args)；
# 将多余的指定参数名的实参打包成一个 dict 传递给字典参数(**kargs)。

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson67_Passing_Arguments_to_Function_3.py
'''
