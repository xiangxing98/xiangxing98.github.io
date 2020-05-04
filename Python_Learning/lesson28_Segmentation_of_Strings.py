# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson28_Segmentation_of_Strings.py
@Time    :   2020/05/04 11:13:19
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''


# here put the import lib
from random import choice


# split() 会把字符串按照其中的空格进行分割，分割后的每一段都是一个新的字符串，
# 最终返回这些字符串组成一个list。于是得到
sentence = 'I am an English sentence'
print(sentence.split())
# ['I', 'am', 'an', 'English', 'sentence']

# 原来字符串中的空格不再存在。
# 除了空格外，split()同时也会按照换行符\n，制表符\t进行分割。所以应该说，split默认是按照空白字符进行分割。
# 之所以说默认，是因为split还可以指定分割的符号。比如你有一个很长的字符串

section = 'Hi. I am the one. Bye.'
print(section.split('.'))
# ['Hi', ' I am the one', ' Bye', '']

# 这时候，'.'作为分割符被去掉了，而空格仍然保留在它的位置上。
# 注意最后那个空字符串。每个'.'都会被作为分割符，即使它的后面没有其他字符，也会有一个空串被分割出来。例如
print("--Start--")
print('aaa'.split('a'))
print("--End--")
# ['', '', '', '']
# 将会得到['', '', '', '']，由四个空串组成的list。

"""
在昨天代码的基础上，我们加上胜负判断，如果5轮结束之后是平分，就继续踢。

所以我们把一轮的过程单独拿出来作为一个函数kick，在5次循环之后再加上一个while循环。

另外，这里把之前的score_you和score_com合并成了一个score数组。
这里的原因是，要让kick函数里用到外部定义的变量，需要使用全局变量的概念。
暂时想避免说这个，而用list不存在这个问题。
（但希望你不要觉得在函数里使用外面定义的变量很自然，后面我们会具体分析）

"""

print("--Start--")

score = [0, 0]
direction = ['left', 'center', 'right']


def kick():
    print('==== You Kick! ====')
    print('Choose one side to shoot:')
    print('left, center, right')
    you = input()
    print('You kicked ' + you)
    com = choice(direction)
    print('Computer saved ' + com)
    if you != com:
        print('得分-Goal!')
        score[0] += 1
    else:
        print('被防守截住了，Oops...')
    print('Score: %d(you) - %d(com)\n' % (score[0], score[1]))

    print('==== You Save! ====')
    print('Choose one side to save:')
    print('left, center, right')
    you = input()
    print('You saved ' + you)
    com = choice(direction)
    print('Computer kicked ' + com)
    if you == com:
        print('你截住了球，Saved!')
    else:
        print('你没有截住球，电脑得分，Oops...')
        score[1] += 1
    print('Score: %d(you) - %d(com)\n' % (score[0], score[1]))


for i in range(5):
    print('==== Round %d ====' % (i + 1))
    kick()

while (score[0] == score[1]):
    i += 1
    print('==== Round %d ====' % (i + 1))
    kick()

if score[0] > score[1]:
    print('You Win!')
else:
    print('You Lose.')

print("--End--")

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson28_Segmentation_of_Strings.py
'''
