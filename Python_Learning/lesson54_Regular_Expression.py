# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson54_Regular_Expression.py
@Time    :   2020/05/05 10:44:29
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

# 如果我们只想找到“hi”这个单词，而不把包含它的单词也算在内，
# 那就可以使用“\bhi\b”这个正则表达式。
# 在以前的字符串处理中，我们已经见过类似“\n”这种特殊字符。
# 在正则表达式中，这种字符更多，以后足以让你眼花缭乱。

# “\b”在正则表达式中表示单词的开头或结尾，空格、标点、换行都算是单词的分割。break
# 而“\b”自身又不会匹配任何字符，它代表的只是一个位置。所以单词前后的空格标点之类不会出现在结果里。
# 在前面那个例子里，“\bhi\b”匹配不到任何结果。
# 但“\bhi”的话就可以匹配到1个“hi”，出自“his”。
# 用这种方法，你可以找出一段话中所有单词“Hi”，想一下要怎么写。

# 在正则表达式中，[]表示满足括号中任一字符。
# 比如“[hi]”，它就不是匹配“hi”了，而是匹配“h”或者“i”。

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson54_Regular_Expression.py
'''
