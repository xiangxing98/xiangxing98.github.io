# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson60_Timer.py
@Time    :   2020/05/05 13:06:03
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''


# here put the import lib
import time


# 在计算机领域有一个特殊的时间，叫做epoch，它表示的时间是1970-01-01 00:00:00 UTC。
# Python中time模块的一个方法time.time()
# 返回的就是从epoch到当前的秒数（不考虑闰秒）。这个值被称为unix时间戳。

starttime = time.time()
print('start:%f' % starttime)
for i in range(10):
    print(i)
endtime = time.time()
print('end:%f' % endtime)
print('total time:%f' % (endtime-starttime))
# start:1588655837.187204
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# end:1588655837.196280
# total time:0.009077

# time.sleep(secs)它可以让程序暂停secs秒。例如：
print(1, "pause 1 seconds")
time.sleep(1)
print(3, "pause 3 seconds")
time.sleep(3)
print(5, "pause 5 seconds")
time.sleep(5)
print(5)
# 在抓取网页的时候，适当让程序sleep一下，可以减少短时间内的请求，提高请求的成功率。

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson60_Timer.py
'''
