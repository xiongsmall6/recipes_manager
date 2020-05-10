#!/user/bin/env python
# -*- coding: utf-8 -*-

"""
@File  : manage.py
@desc: 启动脚本
"""
from flask_cors import CORS
from app import create_app

import pymysql
pymysql.install_as_MySQLdb()

app = create_app('env')
CORS(app, supports_credentials=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)


