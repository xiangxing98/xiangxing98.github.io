# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson48_Object_Oriented_Programming_3.py
@Time    :   2020/05/04 22:27:45
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''


# here put the import lib
# process-oriented; procedure-oriented; Structure-Oriented

# 假设我们有一辆汽车，我们知道它的速度(60km/h)，以及A、B两地的距离(100km)。
# 要算出开着这辆车从A地到B地花费的时间。（很像小学数学题是吧？）

# 面向过程的方法：
speed = 60.0
distance = 100.0
time = distance / speed
print(time)


class Car:
    speed = 0

    def drive(self, distance):
        time = distance / self.speed
        print(time)


car = Car()
car.speed = 60.0
car.drive(100.0)

# 看上去似乎面向对象没有比面向过程更简单，反而写了更多行代码。
# 但是，如果我们让题目再稍稍复杂一点。
# 假设我们又有了一辆更好的跑车，它的速度是150km/h，
# 然后我们除了想从A到B，还要从B到C（距离200km）。
# 要求分别知道这两种车在这两段路上需要多少时间。

# 面向过程的方法：
speed1 = 60.0
distance1 = 100.0
time1 = distance1 / speed1
print(time1)

distance2 = 200.0
time2 = distance2 / speed1
print(time2)

speed2 = 150.0
time3 = distance1 / speed2
print(time3)

time4 = distance2 / speed2
print(time4)


# 面向对象的方法：
class Car:
    speed = 0

    def drive(self, distance):
        time = distance / self.speed
        print(time)


car1 = Car()
car1.speed = 60.0
car1.drive(100.0)
car1.drive(200.0)
# 1.6666666666666667
# 3.3333333333333335

car2 = Car()
car2.speed = 150.0
car2.drive(100.0)
car2.drive(200.0)
# 0.6666666666666666
# 1.3333333333333333

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson48_Object_Oriented_Programming_3.py
'''
