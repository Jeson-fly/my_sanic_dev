#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  @Time     : 2023/3/5 10:05
  @Author   : lining
  @email    : 18810578664@163.com
  @des      : 作者
"""
from sanic.views import HTTPMethodView
from sanic import Request
from sanic import json


class AuthorHttpMethod(HTTPMethodView):
    decorators = []

    async def get(self, request: Request):
        args = request.args
        return json({"key": "author view", "args": args})

    async def post(self, request: Request):
        """post请求"""

    async def put(self,request:Request):
        """put请求"""
