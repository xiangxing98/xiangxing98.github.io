# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson55_Regular_Expression_2.py
@Time    :   2020/05/05 11:02:44
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''

# here put the import lib
import re


text = "Hi, I am Shirley Hilton. I am his wife."
m = re.findall(r"[Hh]i", text)
if m:
    print(m)
else:
    print('not match')
# ['Hi', 'hi', 'Hi', 'hi']

# raw对字符串不进行转义
# 加上了“r”，就表示不要去转义字符串中的任何字符，保持它的原样
print("\bhi")
# hi
print(r"\bhi")
# \bhi
print("\\bhi")
# \bhi

# 两个符号“.”和“*”，顺带说下“\S”和“?”
text = "Hi, I am Shirley Hilton. I am his wife."
m = re.findall(r"i.", text)
if m:
    print(m)
else:
    print('not match')
# ['i,', 'ir', 'il', 'is', 'if']

# 直接用“.”去匹配
m = re.findall(r".", text)
if m:
    print(m)
else:
    print('not match')
# ['H', 'i', ',', ' ', 'I', ' ', 'a', 'm', ' ', 'S', 'h', 'i', 'r', 'l', 'e', 
# 'y', ' ', 'H', 'i', 'l', 't', 'o', 'n', '.', ' ', 'I', ' ', 'a', 'm', ' ', 'h',
#  'i', 's', ' ', 'w', 'i', 'f', 'e', '.']

# 与“.”类似的一个符号是“\S”，它表示的是不是空白符的任意字符。注意是大写字符S。
m = re.findall(r"\$.", text)
if m:
    print(m)
else:
    print('not match')

# 从下面一段文本中，匹配出所有s开头，e结尾的单词。
text2 = "site sea sue sweet see case sse ssee loses"
m = re.findall(r"\bs\S*e\b", text2)
if m:
    print(m)
else:
    print('not match')
# ['site', 'sue', 'see', 'sse', 'ssee']

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson55_Regular_Expression_2.py
'''
