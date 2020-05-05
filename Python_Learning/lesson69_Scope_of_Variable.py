# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson69_Scope_of_Variable.py
@Time    :   2020/05/05 16:40:20
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''


# here put the import lib
def func(x):
    print('X in the beginning of func(x): ', x)
    x = 2
    print('X in the end of func(x): ', x)


x = 50
func(x)
print('X after calling func(x): ', x)

# X in the beginning of func(x):  50
# X in the end of func(x):  2
# X after calling func(x):  50

# 变量 x 在函数内部被重新赋值。但在调用了函数之后，x 的值仍然是50。
# 为什么？

# 当函数内部定义了一个变量，无论是作为函数的形参，或是另外定义的变量，
# 它都只在这个函数的内部起作用。函数外即使有和它名称相同的变量，也没有什么关联。
# 这个函数体就是这个变量的作用域。像这样在函数内部定义的变量被称为“局部变量”。

# 要注意的是，作用域是从变量被定义的位置开始。像这样的写法是有问题的：
# undefined name 'y'

# def func():
#     print(y)
#     y = 2
#     print(y)


# func(10)

# 在 Python 的函数定义中，可以给变量名前加上 global 关键字，
# 这样其作用域就不再局限在函数块中，而是全局的作用域。

def func():
    global x
    print('X in the beginning of func(x): ', x)
    x = 2
    print('X in the end of func(x): ', x)


x = 50
func()
print('X after calling func(x): ', x)
# X in the beginning of func(x):  50
# X in the end of func(x):  2
# X after calling func(x):  2

# 函数 func 不再提供参数调用。而是通过 global x 告诉程序：这个 x 是一个全局变量。
# 于是函数中的 x 和外部的 x 就成为了同一个变量。
# 这一次，当 x 在函数 func 内部被重新赋值后，外部的 x 也随之改变。


# more，略复杂的情况，虽然没有指明 global，函数内部还是使用到了外部定义的变量。
def func():
    print('X in the beginning of func(x): ', x)
    # x = 2
    print('X in the end of func(x): ', x)


x = 50
func()
print('X after calling func(x): ', x)
# X in the beginning of func(x):  50
# X in the end of func(x):  50
# X after calling func(x):  50


# x 成为一个局部变量，它的作用域从定义处开始，到函数体末尾结束
# 程序就会报错
# local variable 'x' defined in enclosing scope on
# line referenced before assignment
def func2():
    print('X in the beginning of func(x): ', x)
    x = 2
    print('X in the end of func(x): ', x)


x = 50
func2()
print('X after calling func(x): ', x)
# UnboundLocalError: local variable 'x' referenced before assignment

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson69_Scope_of_Variable.py
'''
