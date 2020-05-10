#!/usr/bin/python
# -*- coding: utf-8 -*-


class RestResultUtil(object):

    def __init__(self, code, msg, data):
        self.code = code
        self.msg = msg
        self.data = data

    @property
    def serialize(self):
        if self.data is None:
            return {'code': self.code, 'msg': self.msg}
        else:
            return {'code': self.code, 'msg': self.msg, 'data': self.data}

