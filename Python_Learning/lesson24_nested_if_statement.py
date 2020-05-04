# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson24_nested_if_statement.py
@Time    :   2020/05/04 07:18:38
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''

# here put the import lib

# lesson23_nested_if_statement
# if 条件1:
#     if 条件2:
#         语句1
#     else:
#         语句2
# else:
#     if 条件2:
#         语句3
#     else:
#         语句4

# judge Which quadrant baseon (x, y) coordinate
# 值得注意的是原点和坐标轴上的点不属于任何象限
# It's important to note that the origin and the points on the coordinate axis
# do not belong to any quadrant
x = 1
y = -2
if y >= 0:
    if x >= 0:
        print("1st Quadrant")
    else:
        print("2nd Quadrant")
else:
    if x < 0:
        print("3rd Quadrant")
    else:
        print("4th Quadrant")
# 4th Quadrant

# improved
print("\n输入坐标，判断象限")
print("----------------------------------------------------------------------")
x = float(input('请输入一个浮点数Input Coordinate x：'))
y = float(input('请输入一个浮点数Input Coordinate y：'))
if y > 0:
    if x > 0:
        print("1st Quadrant")
    elif x == 0:
        print("At Y Coordinate")
    else:
        print("2nd Quadrant")
elif y < 0:
    if x < 0:
        print("3rd Quadrant")
    elif x == 0:
        print("At Y Coordinate")
    else:
        print("4th Quadrant")
else:
    if x != 0:
        print("At X Coordinate")
    else:
        print("At (0,0) Origin")
print("----------------------------------------------------------------------")


# Python3基础 input 输入浮点数，整数，字符串
"""
@Author : 行初心
@Date   : 18-9-24
@Blog   : https://www.cnblogs.com/xingchuxin/p/10433437.html
@Gitee  : gitee.com/zhichengjiu
"""


def main():
    my_float = float(input('请输入一个浮点数：'))
    print(my_float)
    my_int = int(input('请输入一个整数:'))
    print(my_int)
    my_str = input('请输入一个字符串:')
    print(my_str)


if __name__ == '__main__':
    main()


"""
Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html
"""
# cd /f/Github/xiangxing98.github.io/Python_Learning
# python lesson24_nested_if_statement.py
