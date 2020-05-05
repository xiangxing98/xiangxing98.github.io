# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson18_Type_Casting_Bool.py
@Time    :   2020/05/03 14:55:35
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''

# here put the import lib

# 在python中，其他类型转成 bool 类型时，以下数值会被认为是False：
# 为0的数字，包括0，0.0
# 空字符串，包括''，""
# 表示空值的 None
# 空集合，包括()，[]，{}
# 其他的值都认为是True。

# None 是 python 中的一个特殊值，表示什么都没有，
# None和 0、空字符、False、空集合 都不一样。

# 'False' 是一个包含5个字符的字符串，不是空字符，当被转换成bool类型之后，就得到 True。
print(bool('False'))
# True

# 同样 bool(' ') 的结果是 True，一个空格也不能算作空字符串。
print(bool(' '))
# True

# bool('') 才是False。
print(bool(''))
# False


# 在 if、while 等条件判断语句里，判断条件会自动进行一次bool的转换
a = '123'
if a:
    print(bool(a))
    print('1. this is not a blank string')
# True
# 1. this is not a blank string

# equals to
a = '123'
if bool(a) is True:
    print(bool(a) is True)
    print('2. this is not a blank string')
# True
# 2. this is not a blank string

# equals to
a = '123'
if a != '':
    print(a != '')
    print('3. this is not a blank string')
# True
# 3. this is not a blank string

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson18_Type_Casting_Bool.py
'''
