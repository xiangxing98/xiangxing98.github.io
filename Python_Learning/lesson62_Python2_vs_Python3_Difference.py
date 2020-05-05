# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson62_Python2_vs_Python3_Difference.py
@Time    :   2020/05/05 13:51:20
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''

# here put the import lib

# Python2
# print 'this is version 2'
# print('this is version 2')

# Python3
print('this is version 3')

# Python2不换行输出是加上逗号：
# print '*',

# Python3不换行输出
print('Python3不换行输出*', end=' ')

# Python2 input
# value = input()
# text = raw_input()

# 这种情况下，不管你是看着3的教材用2，还是看着2的教材用3，都会踩到这个坑。
# 3里直接拿 input 得到的“数字”比较大小，会报错类型不同无法比较。
# Python3 input
text = input()

# 那么在3里，如何像2一样得到用户输入的一个值呢？方法是 eval()：
value = eval(input())

# 如果你只是需要一个整数值，也可以：
value = int(input())

# 其他差异
# 打开文件不再支持 file 方法，只能用 open
# range不再返回列表，而是一个可迭代的range对象
# 除法 / 不再是整除，而是得到浮点数，整除需要用双斜杠 //

# urllib和urllib2合并成了urllib，常用的urllib2.urlopen()
# 变成了urllib.request.urlopen()

# 字符串及编码相关有大变动，简单来说就是原来的str变成了新的bytes，
# 原来的unicode变成了新的str。
# 具体内容比较多，可以公众号回复 编码，有一篇专门讲3的字符编码问题

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson62_Python2_vs_Python3_Difference.py
'''
