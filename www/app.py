#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

srv_ip = '127.0.0.1'
srv_port = 8000


def index(request):
	return web.Response(body=b'<h1>Awesome</h1>')


@asyncio.coroutine
def init(loop):
	app = web.Application(loop=loop)
	app.router.add_route('GET', '/', index)
	srv = yield from loop.create_server(app.make_handler(), srv_ip, srv_port)
	logging.info('server started ad http://%s:%d...' % (srv_ip, srv_port))
	return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
