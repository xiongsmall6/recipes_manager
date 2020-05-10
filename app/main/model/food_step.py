#!/user/bin/env python
# -*- coding: utf-8 -*-

from app import db


class FoodStep(db.Model):
    # 在数据库中使用的表名
    __tablename__ = 'food_step'

    id = db.Column(db.Integer, primary_key=True)
    food_id = db.Column(db.Integer)
    step_num = db.Column(db.Integer)
    step_info = db.Column(db.String(1024))
    step_image = db.Column(db.String(256))

    # 返回一个具有可读性的字符串表示模型，可以在调试和测试时使用
    def __repr__(self):
        return '<id %r, food_id %r, step_info %r, step_image %r>' % \
               (self.id, self.food_id, self.step_info, self.step_image)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'food_id': self.food_id,
            'step_num': self.step_num,
            'step_info': self.step_info,
            'step_image': self.step_image
        }


