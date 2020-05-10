#!/user/bin/env python
# -*- coding: utf-8 -*-

"""
@File  : __init__.py
@Author: yfxiong2
@desc: 程序的工厂函数
"""
from flask import Flask, current_app, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import InternalServerError, HTTPException
from config import config
import os

db = SQLAlchemy()


def global_exception_handler(e):
    exc = InternalServerError()
    exception = {
        'code': exc.code,
        'name': exc.name
    }
    current_app.logger.exception(e)
    return render_template('error.html', exception=exception), exc.code


def http_exception_handler(e):
    exception = {
        'code': e.code,
        'name': e.name
    }
    current_app.logger.exception(e)
    return render_template('error.html', exception=exception), e.code


# 程序的工厂函数，接收一个程序使用的配置名
def create_app(config_name):
    conf = config[config_name]
    # conf.APP_NAME = os.getenv('APP') or None
    # conf.APP_NAME = 'test'
    static_url_path = None if conf.APP_NAME is None else '/{app_name}/static'.format(app_name=conf.APP_NAME)
    app = Flask(__name__, static_url_path=static_url_path)
    # 配置文件在config.py中定义，其中保存的配置可以用app.config类提供的from_object()方法直接导入程序，配置对象则可以通过名字从config字典中选择
    app.config.from_object(conf)
    # 程序创建并配置好之后，就可以通过调用init_app完成初始化过程
    conf.init_app(app)
    db.init_app(app)

    # 注册蓝本
    from .main import main as main_blueprint
    url_prefix = None if conf.APP_NAME is None else '/{app_name}'.format(app_name=conf.APP_NAME)
    app.register_blueprint(main_blueprint, url_prefix=url_prefix)

    # 注册全局异常处理
    app.register_error_handler(Exception, global_exception_handler)

    # 注册全局HTTP异常处理
    app.register_error_handler(HTTPException, http_exception_handler)

    return app




