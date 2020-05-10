#!/user/bin/env python
# -*- coding: utf-8 -*-

import datetime

from app import db


def dump_datetime(value):
    if value is None:
        return None
    return value.strftime("%Y-%m-%d %H:%M:%S")


class User(db.Model):
    # 在数据库中使用的表名
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(128))
    nike_name = db.Column(db.String(512))
    user_image = db.Column(db.String(512))
    password = db.Column(db.String(512))
    gender = db.Column(db.Integer)  # 1男 2 女
    age = db.Column(db.Integer)
    create_time = db.Column(db.DateTime(), default=datetime.datetime.now)

    # 返回一个具有可读性的字符串表示模型，可以在调试和测试时使用
    def __repr__(self):
        return '<id %r, user_name %r, nike_name %r, user_image %r, create_time %r>' % \
               (self.id, self.user_name, self.nike_name, self.user_image, self.create_time)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'user_name': self.user_name,
            'nike_name': self.nike_name,
            'user_image': self.user_image,
            'password': self.password,
            'gender': self.gender,
            'age': self.age,
            'create_time': dump_datetime(self.create_time),
        }


