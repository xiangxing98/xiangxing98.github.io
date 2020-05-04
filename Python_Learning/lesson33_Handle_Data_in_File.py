# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson33_Handle_Data_in_File.py
@Time    :   2020/05/04 15:33:39
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''


# here put the import lib

"""
scores.txt
刘备 23 35 44 47 51
关羽 60 77 68
张飞 97 99 89 91
诸葛亮 100
"""

# Read File
f = open('scores.txt', encoding='utf-8')
# f = open('scores.txt', encoding='gbk')
# UnicodeDecodeError: 'gbk' codec can't decode byte 0xa4 in position 4: illegal multibyte sequence

# 取得文件中的数据
lines = f.readlines()
print(lines)
# ['刘备 23 35 44 47 51\n', '关羽 60 77 68\n', '张飞 97 99 89 91\n', '诸葛亮 100']
f.close()

results = []

# 对每一条数据进行处理。按照空格，把姓名、每次的成绩分割开：
for line in lines:
    data = line.split()
    print(data)
    # ['刘备', '23', '35', '44', '47', '51']
    # ['关羽', '60', '77', '68']
    # ['张飞', '97', '99', '89', '91']
    # ['诸葛亮', '100']

    # 如何把一个学生的几次成绩合并，并保存起来呢？我的做法是：
    # 对于每一条数据，都新建一个字符串，把学生的名字和算好的总成绩保存进去。
    # 最后再把这些字符串一起保存到文件中：
    sum = 0
    score_list = data[1:]  # 学生各门课的成绩列表

    for score in score_list:
        sum += int(score) # 字符串转化为整数，求和
    result = '%s\t: %d\n' % (data[0], sum)  # 名字和总分
    print(result)

    # 这里几个要注意的点：
    # 对于每一行分割的数据，data[0]是姓名，data[1:]是所有成绩组成的列表。
    # 每次循环中，sum都要先清零。
    # score是一个字符串，为了做计算，需要转成整数值int。
    # result中，我加了一个制表符\t和换行符\n，让输出的结果更好看些。

    # 得到一个学生的总成绩后，把它添加到一个list中。
    results.append(result)
    # results需要在整个for循环之前初始化 results = []

print(results)
# ['刘备\t: 200\n', '关羽\t: 205\n', '张飞\t: 376\n', '诸葛亮\t: 100\n']

# 最后，全部成绩处理完毕后，把results中的内容保存至文件。
# 因为results是一个字符串组成的list，这里我们直接用writelines方法：
output = open('result.txt', 'w', encoding='utf8')
output.writelines(results)
output.close()


"""
# FUll code

f = open('scores.txt', encoding='gbk')
lines = f.readlines()
# print(lines)
f.close()

results = []

for line in lines:
   # print (line)
   data = line.split()
   # print (data)

   sum = 0
   score_list = data[1:]
   for score in score_list:
       sum += int(score)
   result = '%s \t: %d\n' % (data[0], sum)
   # print (result)

   results.append(result)

# print (results)
output = open('result.txt', 'w', encoding='gbk')
output.writelines(results)
output.close()

"""


'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson33_Handle_Data_in_File.py
'''
