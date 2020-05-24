# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
@File    :   lesson80_Fetching_And_Parsing_Stock_Data.py
@Time    :   2020/05/06 21:43:26
@Author  :   Stone_Hou
@Version :   1.0
@Contact :   xiangxing985529@163.com
@License :   (C)Copyright 2010-2020, Stone_Hou
@Desc    :   None
@Refer   :   https://github.com/xiangxing98
'''


# here put the import lib
import requests


# 这次我们抓取的目标是网易财经的股票板块，
# 我们首先分析一下链接
# http://quotes.money.163.com/trade/lsjysj_603088.html?year=2018&season=1。
# 按照链接的格式，我们拼接好股票代码、年份和季度：

url = "http://quotes.money.163.com/trade/lsjysj_" + \
    key + ".html?year=" + year + "&season=" + season

# 拼接好链接后，使用requests库获取页面的内容：
requests.get(url)
self.parse_pager(content.content, item["code"])

# 考虑到网络请求可能会失败，我们在请求失败时设置多次重新请求(最多8次)，
# 如果多次请求后仍然失败，则将请求的相关内容存储到error_logs中：
# 请求失败后重新请求(最多8次)
max_try = 8
for tries in range(max_try):
    try:
        content = requests.get(url)
        self.parse_pager(content.content, item["code"])
        break
    except Exception:
        if tries < (max_try - 1):
            sleep(2)
            continue
        else:
            add_error_logs("crawl_error", "501", key)


import sys
listone = sys.path
print("添加sit-package前import搜索路径为：")
print("list")
sys.path.append("你的sit-package路径")
print("添加sit-package后import搜索路径为：")
print("list")

'''
# Reference:
https://www.cnblogs.com/xingchuxin/p/10433444.html

# Running Code:
cd /f/Github/xiangxing98.github.io/Python_Learning
python lesson80_Fetching_And_Parsing_Stock_Data.py
'''
