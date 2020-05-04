# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson45_Check_Out_Weather_3.py
@Time    :   2020/05/04 21:56:40
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
'''


# here put the import lib
import requests

"""
# 使用requests库打开一个链接的方法很简单：
req = requests.get('http://www.baidu.com')
print(req)
# <Response [200]>
# 返回了一个 Response 和一个数字，其中数字 200 就代表请求成功。

req.encoding = 'utf8'
content = req.text
print(content)
"""

# 之所以能知道一个城市的天气，是因为用了这样一个天气查询接口：
# http://wthrcdn.etouch.cn/weather_mini?city=北京

# 回到我们的查天气程序，我们首先要获取用户输入，
# 拼接成要请求的 url 地址，并且用requests进行请求
while True:
    city = input('请输入城市,回车退出:\n')
    if not city:
        break

    # 为了防止在请求过程中出错，我加上了一个异常处理
    try:
        req = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=%s' % city)
    except:
        print("查询失败")
        break

    # print(req.text)

    # 可以看到，已经拿到了json格式的天气信息。下一课我们再来处理它。
    """
    {
        "data": {
            "yesterday": {
                "date": "3日星期日",
                "high": "高温 34℃",
                "fx": "南风",
                "low": "低温 24℃",
                "fl": "<![CDATA[<3级]]>",
                "type": "多云"
            },
            "city": "长沙",
            "forecast": [
                {
                    "date": "4日星期一",
                    "high": "高温 34℃",
                    "fengli": "<![CDATA[<3级]]>",
                    "low": "低温 23℃",
                    "fengxiang": "南风",
                    "type": "多云"
                },
                {
                    "date": "5日星期二",
                    "high": "高温 29℃",
                    "fengli": "<![CDATA[<3级]]>",
                    "low": "低温 21℃",
                    "fengxiang": "西北风",
                    "type": "小雨"
                },
                {
                    "date": "6日星期三",
                    "high": "高温 28℃",
                    "fengli": "<![CDATA[<3级]]>",
                    "low": "低温 22℃",
                    "fengxiang": "东风",
                    "type": "小雨"
                },
                {
                    "date": "7日星期四",
                    "high": "高温 32℃",
                    "fengli": "<![CDATA[<3级]]>",
                    "low": "低温 24℃",
                    "fengxiang": "南风",
                    "type": "多云"
                },
                {
                    "date": "8日星期五",
                    "high": "高温 33℃",
                    "fengli": "<![CDATA[<3级]]>",
                    "low": "低温 21℃",
                    "fengxiang": "北风",
                    "type": "阵雨"
                }
            ],
            "ganmao": "相对今天出现了较大幅度降温，较易发生感冒，体质较弱的朋友请注意适当防护。",
            "wendu": "30"
        },
        "status": 1000,
        "desc": "OK"
    }
    """

    # 我们可以直接用requests模块的json()方法，
    # 将请求得到的json格式的字符串直接转成一个真正的字典。
    dic_city = req.json()
    # print(dic_city)

    # print(type(req.text))
    # <class 'str'>
    # print(type(req.json()))
    # <class 'dict'>

    # 首先使用字典的get方法，若城市名错误返回的字典中没有’data‘这个键，
    # 程序不会报错，而是返回 None
    city_data = dic_city.get('data')

    # 接着，分别输出查询城市当天的日期、最高温、最低温和天气类型，或者进行没有找到城市时的处理：
    if city_data:
        city_forecast = city_data['forecast'][0]  # 下面的都可以换成'get'方法
        print(city_forecast.get('date'))
        print(city_forecast.get('high'))
        print(city_forecast.get('low'))
        print(city_forecast.get('type'))
    else:
        print('未获得')

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson45_Check_Out_Weather_3.py
'''
