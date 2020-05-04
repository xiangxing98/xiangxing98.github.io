# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson30_String_Index_Slice.py
@Time    :   2020/05/04 13:47:07
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''


# here put the import lib

# 通过for...in可以遍历字符串中的每一个字符。
word = 'helloword'
for c in word:
    print(c)
# h
# e
# l
# l
# o
# w
# o
# r
# d

# 通过[]加索引的方式，访问字符串中的某个字符。
print("--Start--")
print(word[0])
print(word[-2])
print("--End--")
# --Start--
# h
# r
# --End--

# 与list不同的是，字符串不能通过索引访问去更改其中的字符。
# word[1] = 'a'
# TypeError: 'str' object does not support item assignment

# 通过两个参数，截取一段子串，具体规则和list相同。
print(word[5:7])
print(word[:-5])
print(word[:])
# wo
# hell
# helloword

# join方法也可以对字符串使用，作用就是用连接符把字符串中的每个字符重新连接成一个新字符串。
newword = ','.join(word)
print(newword)
# h,e,l,l,o,w,o,r,d

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson30_String_Index_Slice.py
'''
