#!/user/bin/env python
# -*- coding: utf-8 -*-

"""
@File  : __init__.py
@desc: 创建蓝本
"""

from flask import Blueprint

# 实例化一个Blueprint类对象可以创建蓝本
main = Blueprint('main', __name__)

# 在脚本的末尾导入是为了避免循环导入依赖
from . import views
