#!/user/bin/env python
# -*- coding: utf-8 -*-

from app import db


class FoodMaterial(db.Model):
    # 在数据库中使用的表名
    __tablename__ = 'food_material'

    id = db.Column(db.Integer, primary_key=True)
    food_id = db.Column(db.Integer)
    material_name = db.Column(db.String(512))
    material_unit = db.Column(db.String(64))

    # 返回一个具有可读性的字符串表示模型，可以在调试和测试时使用
    def __repr__(self):
        return '<id %r, food_id %r, material_name %r, material_unit %r>' % \
               (self.id, self.food_id, self.material_name, self.material_unit)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'food_id': self.food_id,
            'material_name': self.material_name,
            'material_unit': self.material_unit
        }


