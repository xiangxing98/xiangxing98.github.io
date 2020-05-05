# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson72_multi_thread.py
@Time    :   2020/05/05 17:56:35
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''


# here put the import lib
import requests
import threading

# python 里有一个 threading 模块，其中提供了一个函数：

# threading.Thread(target=function, args=(), kwargs={})

# function 是开发者定义的线程函数，
# args 是传递给线程函数的参数，必须是tuple类型，
# kwargs 是可选参数，字典类型。

# 调用 threading.Thread 之后，会创建一个新的线程，
# 参数 target 指定线程将要运行的函数，
# args 和 kwargs 则指定函数的参数来执行 function 函数。

# 改写一下前面抓取城市的天气的代码，将抓取的部分放在一个函数中：


def get_weather(city):
    req = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=%s' % city)
    dic_city = req.json()

    city_data = dic_city.get('data')  # 没有’data‘的话返回 []
    print(city_data.get('city'))

    if city_data:
        city_forecast = city_data['forecast'][0]  # 下面的都可以换成'get'方法
        print('============================================================')
        print(
            city_data.get('city'),
            city_forecast.get('date'),
            city_forecast.get('high'),
            city_forecast.get('low'),
            city_forecast.get('type')
        )
        print('============================================================')
    else:
        print('未获得')
    # print()


# 之后，程序采用了三个循环，在第一个循环中，针对每一个城市，都创建了一个新线程，
# 并将线程加入到一个列表中，用于之后的启动。

threads = []
cities = ['北京', '南京', '上海', '深圳', '广州', '杭州', '苏州', '天津', '西安', '成都']
files = range(len(cities))
for i in files:  # 创建线程
    t = threading.Thread(target=get_weather, args=(cities[i],))
    threads.append(t)

# 在第二个循环中，start 正式开启子线程；
for i in files:
    threads[i].start()

# 在第三个循环中，join 用来同步数据，主线程运行到这一步，
# 将会停下来等待子线程运行完毕。
# 没有这句，主线程则会忽略子线程，运行完自己的代码后结束程序。
for i in files:
    threads[i].join()

print('结束获取天气资讯')

# 从输出结果可以看出：

# 在程序刚开始运行时，已经发送所有请求
# 收到的请求并不是按发送顺序，先收到就先显示
# 同样记录了所有10个城市的天气

# 所以，对于这种耗时长，但又独立的任务，使用多线程可以大大提高运行效率。
# 但在代码层面，可能额外需要做一些处理，保证结果正确。
# 如上例中，如果需要按输入列表城市顺序进行输出，就要另行排序。

# 多线程通常会用在网络收发数据、文件读写、用户交互等待之类的操作上，
# 以避免程序阻塞，提升用户体验或提高执行效率。

# 多线程的实现方法不止这一种。
# 另外多线程也会带来一些单线程程序中不会出现的问题。这里只是简单地开个头。

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson72_multi_thread.py
'''
