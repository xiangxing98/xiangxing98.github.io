# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson37_dictionary.py
@Time    :   2020/05/04 18:34:17
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''


# here put the import lib

# 键/值对用冒号分割，每个对之间用逗号分割，整个字典包括在花括号中。
# 关于字典的键要注意的是：
# 1.键必须是唯一的；
# 2.键只能是简单对象，比如字符串、整数、浮点数、bool值。list就不能作为键，但是可以作为值。
# d = {key1 : value1, key2 : value2}

score = {
   '萧峰': 95,
   '段誉': 97,
   '虚竹': 89
}

# python字典中的键/值对没有顺序，我们无法用索引访问字典中的某一项，而是要用键来访问。
# 注意，如果你的键是字符串，通过键访问的时候就需要加引号，如果是数字作为键则不用。
print(score['段誉'])
# 97

# 如果你提供的键在字典中不存在，则会报错。另一种访问字典中元素的方法是：
# 这种方法的好处是，即使提供的键不存在，也不会报错，只会返回 None
score.get("慕容复")

# 字典也可以通过for...in遍历：
# 注意，遍历的变量中存储的是字典的键。
print("--Start--")
for name in score:
    print(score[name])
print("--End--")
# --Start--
# 95
# 97
# 89
# --End--

# 如果要改变某一项的值，就直接给这一项赋值：
score['虚竹'] = 91
print("--Start--")
for name in score:
    print(score[name])
print("--End--")
# --Start--
# 95
# 97
# 91
# --End--

# 增加一项字典项的方法是，给一个新键赋值：
score['慕容复'] = 88
print("--Start--")
for name in score:
    print(score[name])
print("--End--")
# --Start--
# 95
# 97
# 91
# 88
# --End--

# 删除一项字典项的方法是del，注意，这个键必须已存在于字典中。
del score['萧峰']

# 如果你想新建一个空的字典，只需要:
d = {}
print(d)
# {}
'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson37_dictionary.py
'''
