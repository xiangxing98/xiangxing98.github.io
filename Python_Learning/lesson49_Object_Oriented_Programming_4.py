# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson49_Object_Oriented_Programming_4.py
@Time    :   2020/05/05 08:24:43
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''

# here put the import lib

# process-oriented; procedure-oriented; Structure-Oriented

# 仍然是从A地到B地，这次除了有汽车，我们还有了一辆自行车！

# 自行车和汽车有着相同的属性：速度（speed）。
# 还有一个相同的方法（drive），来输出行驶/骑行一段距离所花的时间。
# 但这次我们要给汽车增加一个属性：每公里油耗（fuel）。
# 而在汽车行驶一段距离的方法中，除了要输出所花的时间外，还要输出所需的油量。


# 面向对象的方法：
class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def drive(self, distance):
        print('need %f hour(s)' % (distance / self.speed))


class Bike(Vehicle):
    pass


# __init__函数会在类被创建的时候自动调用，用来初始化类。
# 它的参数，要在创建类的时候提供。于是我们通过提供一个数值来初始化speed的值。
# 注意：__init__是python的内置方法，类似的函数名前后是两个下英文划线，
# 如果写错了，则不会起到原本应有的作用。
class Car(Vehicle):
    def __init__(self, speed, fuel):
        Vehicle.__init__(self, speed)
        self.fuel = fuel

    def drive(self, distance):
        Vehicle.drive(self, distance)
        print('need %f fuels' % (distance * self.fuel))


# 创建一个速度为15的自行车对象, 创建一个速度为80、耗油量为0.012的汽车
b = Bike(15.0)
c = Car(80.0, 0.012)

# 行驶100的距离,计算耗时与耗油量
b.drive(100.0)
c.drive(100.0)
# need 6.666667 hour(s)
# need 1.250000 hour(s)
# need 1.200000 fuels

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson49_Object_Oriented_Programming_4.py
'''
