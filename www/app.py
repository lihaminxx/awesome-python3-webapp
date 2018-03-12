#-- coding: utf-8 --

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

# def index(request):
#     return web.Response(body=b'<h1>Awesome</h1>')

def index(request):
    # 原版返回的是一个二进制，所以就下载了
    return web.Response(body='<h1>Awesome</h1>')
#测试结果没有把Awesome用h1显示，而是把 <h1>Awesome</h1> 全部显示在网页上了

# def index(request):
#     return web.Response(body=b'<h1>Awesome</h1>', headers={'content-type':'text/html'})
# #存在一个中文乱码的问题，暂时未解决  ????????????

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

#test git 

#test add to the temporay place  and then rollback 

#add to the 