# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson53_Truth_Table.py
@Time    :   2020/05/05 10:43:26
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''

# here put the import lib
# Truth_Table

'''
为了便于看清，我用<=>来表示等价关系。
<=>左边表示逻辑表达式，<=>右边表示它的结果。

NOT
not False <=> True
not True <=> False
（not的结果与原值相反）

OR
True or False <=> True
True or True <=> True
False or True <=> True
False or False <=> False
（只要有一个值为True，or的结果就是True）

AND
True and False <=> False
True and True <=> True
False and True <=> False
False and False <=> False
（只要有一个值为False，and的结果就是False）

NOT OR
not (True or False) <=> False
not (True or True) <=> False
not (False or True) <=> False
not (False or False) <=> True

NOT AND
not (True and False) <=> True
not (True and True) <=> False
not (False and True) <=> True
not (False and False) <=> True

!=
1 != 0 <=> True
1 != 1 <=> False
0 != 1 <=> True
0 != 0 <=> False

==
1 == 0 <=> False
1 == 1 <=> True
0 == 1 <=> False
0 == 0 <=> True
'''

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html
https://python666.cn/cls/lesson/55/

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson53_Truth_Table.py
'''