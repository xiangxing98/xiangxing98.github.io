# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson64_List_Comprehension.py
@Time    :   2020/05/05 14:07:00
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''

# here put the import lib
list_1 = [1, 2, 3, 5, 8, 13, 22]
list_2 = []
for i in list_1:
    if i % 2 == 0:
        list_2.append(i)
print(list_2)
# [2, 8, 22]
# 通过循环来遍历列表，对其中的每一个元素进行判断，若模取2的结果为0则添加至新列表中。

# 使用列表解析实现同样的效果：
list_1 = [1, 2, 3, 5, 8, 13, 22]
list_2 = [i for i in list_1 if i % 2 == 0]
print(list_2)
# [2, 8, 22]

# [i for i in list_1] 会把 list_1 中的每一个元素都取出来，构成一个新的列表。
# 如果需要对其中的元素进行筛选，就在后面加上判断条件 if。
# 所以 [i for i in list_1 if i % 2 == 0] 就是把 list_1 中
# 满足 i % 2 == 0 的元素取出来组成新列表。

# 进一步的，在构建新列表时，还可以对于取出的元素做操作。比如，对于原列表中的偶数项，
# 取出后要除以2，则可以通过 [i / 2 for i in list_1 if i % 2 == 0] 来实现。
# 输出为 [1, 4, 11]。

# 用一行 Python 代码实现：把1到100的整数里，能被2、3、5整除的数取出，
# 以分号（;）分隔的形式输出。

my_list = range(1, 101)
print(';'.join([str(i) for i in my_list if i % 2 == 0 and i % 3 == 0 and i % 5 == 0]))


'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson64_List_Comprehension.py
'''
