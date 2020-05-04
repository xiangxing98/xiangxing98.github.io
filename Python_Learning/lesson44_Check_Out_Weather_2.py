# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson44_Check_Out_Weather_2.py
@Time    :   2020/05/04 21:43:17
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''


# here put the import lib
import requests


# 使用requests库打开一个链接的方法很简单：
req = requests.get('http://www.baidu.com')
print(req)
# <Response [200]>
# 返回了一个 Response 和一个数字，其中数字 200 就代表请求成功。

req.encoding = 'utf8'
content = req.text
print(content)

# 之所以能知道一个城市的天气，是因为用了这样一个天气查询接口：
# http://wthrcdn.etouch.cn/weather_mini?city=北京

# 回到我们的查天气程序，我们首先要获取用户输入，
# 拼接成要请求的 url 地址，并且用requests进行请求
while True:
    city = input('请输入城市,回车退出:\n')
    if not city:
        break
    req = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=%s' % city)
    print(req.text)
# 可以看到，已经拿到了json格式的天气信息。下一课我们再来处理它。

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson44_Check_Out_Weather_2.py
'''
