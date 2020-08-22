# -*- encoding: utf-8 -*-
# !/usr/bin/env python
import logging
logging.basicConfig(level=logging.INFO)

import asyncio
import os
import json
import time
from datetime import datetime

from aiohttp import web, web_runner


routes = web.RouteTableDef()


@routes.get('/')
# 请求处理器返回的Response实例传入参数content_type='text/html'，否则会出现下载页面。
async def index(request):
    # return web.Response(body=b'<h1>Awesome</h1>')
    return web.Response(body=b',<h1>Awesome, Hou</h1><p>@2020-08-22</p>',
                        content_type='text/html')


# @asyncio.coroutine
# asyncio，推荐的写法是 async + await
def init():
    app = web.Application()
    app.add_routes([web.get('/', index)])  # 多看看官方文档，aiohttp和asyncio都要看
    logging.info('server started at http://127.0.0.1:8080...')
    web.run_app(app, host='127.0.0.1', port=8080)


init()
