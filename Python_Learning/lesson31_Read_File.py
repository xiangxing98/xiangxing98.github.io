# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson31_Read_File.py
@Time    :   2020/05/04 14:34:52
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''


# here put the import lib

# 打开一个文件的命令很简单：
# open('文件名')

# 这里的文件名可以用文件的完整路径，也可以是相对路径。
# 因为我们把要读取的文件和代码放在了同一个文件夹下，所以只需要写它的文件名就够了。
f = open('data.txt')

# read得到其中的内容并打印出来
data = f.read()
print(data)
# data,hello
# da,haha

# 做完对文件的操作之后，记得用close()关闭文件，释放资源。
f.close()

# full code
f = open('data.txt')
data = f.read()
print(data)
f.close()

# 读取文件内容的方法还有
# readline() #读取一行内容
# readlines() #把内容按行读取至一个list中
f2 = open('data.txt')
for line in f2.readlines():
    print(line)

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson31_Read_File.py
'''
