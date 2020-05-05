# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson21_Function_Parameter.py
@Time    :   2020/05/03 18:40:46
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''


# here put the import lib
# 定义的函数里允许调用者提供一些参数
def sayHello(someone):
    print(someone + ' says Hello!')


# Define Another Function，多个参数
def plus(num1, num2):
    print(num1+num2)


# 调用函数，传入参数
sayHello('Stone_Hou')
# Stone_Hou says Hello!

# 调用函数，传入多个参数
plus(1, 10)
# 11

# 调用函数，传入多个参数
x = 3
y = 4
plus(x, y)
# 7

# 在Python中如果condition为 ''，()，[]，{}，None，set()那么该条件为False,否则为True。
# if (condition)：
#     doSomething()

# 1.针对字符串的测试
condition1 = ''
if condition1:
    print('condition1 True')
else:
    print('condition1 False')
# False

condition2 = 'test'
if condition2:
    print('condition2 True')
else:
    print('condition2 False')
# True

# 2.针对原组的测试
condition3 = ()
if condition3:
    print('condition3 True')
else:
    print('condition3 False')
# False

condition4 = (1, 2)
if condition4:
    print('condition4 True')
else:
    print('condition4 False')
# True

# 3.针对列表的测试
condition5 = []
if condition5:
    print('condition5 True')
else:
    print('condition5 False')
# False

condition6 = ['a', 'b']
if condition6:
    print('condition6 True')
else:
    print('condition6 False')
# True

# 4.针对字典的测试
condition7 = {}
if condition7:
    print('condition7 True')
else:
    print('condition7 False')
# False
condition8 = {'k': 'v'}
if condition8:
    print('condition8 True')
else:
    print('condition8 False')
# True

# 5.针对None的测试
condition9 = None
if condition9:
    print('condition9 True')
else:
    print('condition9 False')
# False

# 6.针对set()的测试
condition10 = set()
if condition10:
    print('condition10 True')
else:
    print('condition10 False')
# False

condition11 = condition10.add('a')
if condition11:
    print('condition11 True')
else:
    print('condition11 False')
# True

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson21_Function_Parameter.py
'''
