# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson81_Python3_Commandline_Arguments.py
@Time    :   2020/05/17 15:19:20
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''

# here put the import lib
import sys


"""
Python3 命令行参数
Python 提供了 getopt 模块来获取命令行参数。
$ python test.py arg1 arg2 arg3
Python 中也可以所用 sys 的 sys.argv 来获取命令行参数：
sys.argv 是命令行参数列表。
len(sys.argv) 是命令行参数个数。
注：sys.argv[0] 表示脚本名。
实例
test.py 文件代码如下：
"""
print('参数个数为:', len(sys.argv), '个参数。')
print('参数列表:', str(sys.argv))


"""
getopt模块
getopt模块是专门处理命令行参数的模块，用于获取命令行选项和参数，也就是sys.argv。
命令行选项使得程序的参数更加灵活。支持短选项模式（-）和长选项模式（--）。

该模块提供了两个方法及一个异常处理来解析命令行参数。

getopt.getopt 方法
getopt.getopt 方法用于解析命令行参数列表，语法格式如下：
getopt.getopt(args, options[, long_options])
方法参数说明：

args: 要解析的命令行参数列表。

options: 以字符串的格式定义，options后的冒号(:)
表示该选项必须有附加的参数，不带冒号表示该选项不附加参数。

long_options: 以列表的格式定义，long_options 后的等号(=)表示如果设置该选项，
必须有附加的参数，否则就不附加参数。

该方法返回值由两个元素组成: 第一个是 (option, value) 元组的列表。
第二个是参数列表，包含那些没有'-'或'--'的参数。

另外一个方法是 getopt.gnu_getopt，这里不多做介绍。

"""

"""
Exception getopt.GetoptError
在没有找到参数列表，或选项的需要的参数为空时会触发该异常。

异常的参数是一个字符串，表示错误的原因。属性 msg 和 opt 为相关选项的错误信息。

实例
假定我们创建这样一个脚本，可以通过命令行向脚本文件传递两个文件名，
同时我们通过另外一个选项查看脚本的使用。脚本使用方法如下：
usage: test.py -i <inputfile> -o <outputfile>

test.py 文件代码如下所示：
"""

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson81_Python3_Commandline_Arguments.py

执行以上代码，输出结果为：
参数个数为: 1 个参数。
参数列表: ['lesson81_Python3_Commandline_Arguments.py']

python lesson81_Python3_Commandline_Arguments.py arg1 arg2 arg4
参数个数为: 4 个参数。
参数列表: ['lesson81_Python3_Commandline_Arguments.py', 'arg1', 'arg2', 'arg4']
'''
