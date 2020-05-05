# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson47_Object_Oriented_Programming_2.py
@Time    :   2020/05/04 22:19:46
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''


# here put the import lib
# 今天我们来创建一个类。我们用pass语句，表示一个空的代码块。
class MyClass:
    pass


mc = MyClass()
print(mc)
# <__main__.MyClass object at 0x000001FA2B04A518>
# 这个意思就是说，mc是__main__模块中MyClass来的一个实例（instance），
# 后面的一串十六进制的数字是这个对象的内存地址。


# 我们给这个类加上一些方法：
# 我们给MyClass类增加了一个类变量name，并把它的值设为'Sam'。
# 然后又增加了一个类方法sayHi。
class MyClass:
    name = 'Sam'

    def sayHi(self):
        print('Hello %s' % self.name)


# 调用类变量的方法是“对象.变量名”。你可以得到它的值，也可以改变它的值。

mc = MyClass()
print(mc.name)
# Sam

# 注意到，类方法和我们之前定义的函数区别在于，第一个参数必须为self。
# 而在调用类方法的时候，通过“对象.方法名()”格式进行调用，而不需要额外提供self这个参数的值。
# self在类方法中的值，就是你调用的这个对象本身。
mc.name = 'Lily'
mc.sayHi()
# Hello Lily

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson47_Object_Oriented_Programming_2.py
'''
