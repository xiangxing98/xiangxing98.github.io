# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson32_Write_File.py
@Time    :   2020/05/04 15:13:39
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''


# here put the import lib
# 打开文件我们昨天已经讲过。
# 但python默认是以只读模式打开文件。
# 如果想要写入内容，在打开文件的时候需要指定打开模式为写入：
f = open('output.txt', 'w')
# 'w'就是writing，以这种模式打开文件，原来文件中的内容会被你新写入的内容覆盖掉，如果文件不存在，会自动创建文件。
f.write('a string you want to write')
f.close()

data = 'I will be in a file.\nSo cool!'
out = open('output.txt', 'a')
out.write(data)
out.close()

my_file = open('output.txt', 'r')
data = my_file.read()
print(data)
my_file.close()
# a string you want to writeI will be in a file.
# So cool!

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson32_Write_File.py
'''
