# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson1_Python3_Basic_Syntax.py
@Time    :   2020/05/17 14:52:40
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''

# here put the import lib


# 注释
# Python中单行注释以 # 开头，实例如下：
# 第一个注释
print("Hello, Python!")  # 第二个注释

# 多行注释可以用多个 # 号，还有 ''' 和 """：
# !/usr/bin/python3

# 第一个注释
# 第二个注释

'''
第三注释
第四注释
'''

"""
第五注释
第六注释
"""

# Line and indent
if True:
    print("True")
else:
    print("False")

# 多行语句-使用反斜杠(\)来实现多行语句
item_one = 2
item_two = 3
item_three = 5

total = item_one + \
    item_two + \
    item_three

# 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)，例如：
total = ['item_one', 'item_two', 'item_three',
         'item_four', 'item_five']

"""
数字(Number)类型
python中数字有四种类型：整数、布尔型、浮点数和复数。

int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
bool (布尔), 如 True。
float (浮点数), 如 1.23、3E-2
complex (复数), 如 1 + 2j、 1.1 + 2.2j

字符串(String)
python中单引号和双引号使用完全相同。
使用三引号('''或\"\"\")可以指定一个多行字符串。
转义符 '\'
反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
如 r"this is a line with \n" 则\n会显示，并不是换行。
按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
字符串可以用 + 运算符连接在一起，用 * 运算符重复。
Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
Python中的字符串不能改变。
Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
字符串的截取的语法格式如下：变量[头下标:尾下标:步长]

"""

word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成
可以由多行组成
可以由多行组成
可以由多行组成"""


str = 'Python'

print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始后的所有字符
print(str * 2)             # 输出字符串两次
print(str + '你好')        # 连接字符串

print('------------------------------')

print('hello\nPython')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nPython')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
# 这里的 r 指 raw，即 raw string。
"""
输出结果为：
Python
Python
P
tho
thon
PythonPython
Python你好
------------------------------
hello
Python
hello\nPython
"""

"""
空行
函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。
类和函数入口之间也用一行空行分隔，以突出函数入口的开始。

空行与代码缩进不同，空行并不是Python语法的一部分。
书写时不插入空行，Python解释器运行也不会出错。
但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。

记住：空行也是程序代码的一部分。

等待用户输入
执行下面的程序在按回车键后就会等待用户输入：
input("\n\n按下 enter 键后退出。")

同一行显示多条语句
Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：
import sys; x = 'Python'; sys.stdout.write(x + '\n')

多个语句构成代码组
缩进相同的一组语句构成一个代码块，我们称之代码组。

像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，
该行之后的一行或多行代码构成代码组。

我们将首行及后面的代码组称为一个子句(clause)。

如下实例：
if expression :
   suite
elif expression :
   suite
else :
   suite
"""

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson1_Python3_Basic_Syntax.py
'''
