#!/user/bin/env python
# -*- coding: utf-8 -*-

import datetime

from app import db


def dump_datetime(value):
    if value is None:
        return None
    return value.strftime("%Y-%m-%d %H:%M:%S")


class Food(db.Model):
    # 在数据库中使用的表名
    __tablename__ = 'food'

    id = db.Column(db.Integer, primary_key=True)
    food_name = db.Column(db.String(128))
    food_info = db.Column(db.String(512))
    food_image = db.Column(db.String(512))
    food_type = db.Column(db.Integer)
    praise = db.Column(db.Integer)
    collections = db.Column(db.Integer)
    create_user = db.Column(db.String(128))
    create_time = db.Column(db.DateTime(), default=datetime.datetime.now)

    # 返回一个具有可读性的字符串表示模型，可以在调试和测试时使用
    def __repr__(self):
        return '<id %r, food_name %r, food_type %r, create_user %r, create_time %r>' % \
               (self.id, self.food_name, self.food_type, self.create_user, self.create_time)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'food_name': self.food_name,
            'food_info': self.food_info,
            'food_image': self.food_image,
            'food_type': self.food_type,
            'praise': self.praise,
            'collections': self.collections,
            'create_user': self.create_user,
            'create_time': dump_datetime(self.create_time),
        }


