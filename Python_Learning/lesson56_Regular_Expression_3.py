# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson56_Regular_Expression_3.py
@Time    :   2020/05/05 12:04:16
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''


# here put the import lib
import re


# 从下面一段文本中，匹配出所有s开头，e结尾的单词。
text2 = "site sea sue sweet see case sse ssee loses"
m = re.findall(r"\bs\S*e\b", text2)
if m:
    print(m)
else:
    print('not match')
# ['site', 'sue', 'see', 'sse', 'ssee']


# 匹配手机号
# 匹配手机号，其实就是找出一串连续的数字。更进一步，是11位，以1开头的数字。
# 匹配数字，我们可以用[0123456789]
# 由于它们是连续的字符，有一种简化的写法：[0-9]。类似的还有[a-zA-Z]的用法。
# 还有另一种表示数字的方法：\d
# 要表示任意长度的数字，就可以用[0-9]*或者\d*

# 但要注意的是，*表示的任意长度包括0，也就是没有数字的空字符也会被匹配出来。
# 一个与*类似的符号+，表示的则是1个或更长。
# 所以要匹配出所有的数字串，应当用[0-9]+, 或者\d+

# 如果要限定长度，就用{}代替+，大括号里写上你想要的长度。比如11位的数字：\d{11}
# 想要再把第一位限定为1，就在前面加上1，后面去掉一位：1\d{10}
def main(text='13581974134'):
    if text:
        tel = text
    else:
        tel = input("请输入手机号:")

    # ret = re.match(r"1[35678]\d{9}", tel)
    # 由于手机号位数大于11位也能匹配成功，所以修改如下：
    ret = re.match(r"^1[35678]\d{9}$", tel)

    if ret:
        print(ret)
        print("匹配成功")
    else:
        print("匹配失败")


if __name__ == "__main__":
    main(text='13581974135')

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson56_Regular_Expression_3.py
'''
