#!/user/bin/env python
# -*- coding: utf-8 -*-



import logging
import os
from logging.handlers import RotatingFileHandler

basedir = os.path.abspath(os.path.dirname(__file__))


class InfoFilter(logging.Filter):
    def filter(self, record):
        if logging.INFO <= record.levelno < logging.ERROR:
            return super().filter(record)
        else:
            return 0


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guss string'
    # 当关闭数据库是否自动提交事务
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    LOG_PATH = os.path.join(basedir, 'logs')
    LOG_PATH_ERROR = os.path.join(LOG_PATH, 'error.log')
    LOG_PATH_INFO = os.path.join(LOG_PATH, 'info.log')
    LOG_FILE_MAX_BYTES = 100 * 1024 * 1024
    # 轮转数量是 10 个
    LOG_FILE_BACKUP_COUNT = 10

    LOGGING_FORMATTER = logging.Formatter(
        '%(asctime)s %(levelname)s %(process)d %(thread)d '
        '[%(pathname)s:%(lineno)s]: %(message)s')
    APP_NAME = 'food'

    @classmethod
    def init_app(cls, app):
        # FileHandler Info
        file_handler_info = RotatingFileHandler(filename=cls.LOG_PATH_INFO, encoding='utf-8')
        file_handler_info.setFormatter(cls.LOGGING_FORMATTER)
        file_handler_info.setLevel(logging.INFO)
        info_filter = InfoFilter()
        file_handler_info.addFilter(info_filter)
        app.logger.addHandler(file_handler_info)

        # FileHandler Error
        file_handler_error = RotatingFileHandler(filename=cls.LOG_PATH_ERROR, encoding='utf-8')
        file_handler_error.setFormatter(cls.LOGGING_FORMATTER)
        file_handler_error.setLevel(logging.ERROR)
        app.logger.addHandler(file_handler_error)


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost:3306/cookbook'
    SQLALCHEMY_ECHO = True
    DEBUG = True
    ENV = 'dev'
    JSON_AS_ASCII = False



class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost:3306/cookbook'
    SQLALCHEMY_ECHO = True
    DEBUG = False
    ENV = 'pro'
    JSON_AS_ASCII = False


config = {
    'env': DevelopmentConfig
}
