from app.main.model.food import Food
from app.main.model.food_material import FoodMaterial
from app.main.model.food_step import FoodStep
from app import db
from sqlalchemy import text
import datetime


def add_food(food):
    """ 添加模型"""
    try:
        db.session.add(food)
        db.session.commit()
        return food
    except Exception as e:
        db.session.rollback()
        raise e


def query_food_random(food_type):
    """根据类型查询用户选择图片"""
    try:
        select_params_dict = {
            "food_type": food_type
        }
        sql = "select * from food where FOOD_TYPE= :food_type ORDER BY RAND() limit 2"
        bind_sql = text(sql)
        resproxy = db.session.connection().execute(bind_sql, select_params_dict)
        info_list = resproxy.fetchall()
        result_list = list()
        if info_list:
            for item in info_list:
                result_list.append({"id": item[0], "food_name": item[1],
                                    "food_info": item[2], "food_image": item[3],
                                    "food_type": item[4], "praise": item[5],
                                    "collections": item[6], "create_time": item[7],
                                    "create_user": item[8]})
        return result_list
    except Exception as e:
        raise e


def add_food_material(food_material_list):
    """ 添加模型"""
    try:

        db.session.execute(
            FoodMaterial.__table__.insert(),
            food_material_list
        )

        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e


def add_food_step(food_step_list):
    """ 添加模型"""
    try:
        db.session.execute(
            FoodStep.__table__.insert(),
            food_step_list
        )
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e


def query_food(type):
    try:
        model_list = db.session.query(Food).filter(Food.food_type == type)\
            .order_by(Food.create_time.desc()).limit(2).all()
        return model_list
    except Exception as e:
        db.session.rollback()
        raise e


def query_food_by_id(food_id):
    try:
        food = db.session.query(Food).filter(Food.id == food_id).first()
        return food
    except Exception as e:
        db.session.rollback()
        raise e


def query_material(food_id):
    try:
        material_list = db.session.query(FoodMaterial).filter(FoodMaterial.food_id == food_id).all()
        return material_list
    except Exception as e:
        db.session.rollback()
        raise e


def query_step(food_id):
    try:
        step_list = db.session.query(FoodStep).filter(FoodStep.food_id == food_id).order_by(FoodStep.step_num.asc()).all()
        return step_list
    except Exception as e:
        db.session.rollback()
        raise e


def query_food_list(page, limit, create_user, food_type, search):
    """根据条件查询食谱"""
    try:
        filter_param = []
        offset = (page - 1) * limit
        if create_user:
            filter_param.append(Food.create_user == create_user)
        if food_type:
            filter_param.append(Food.food_type == food_type)
        if search:
            filter_param.append(Food.food_name.like("%" + search + "%"))
        food_list = Food.query.filter(*filter_param).limit(limit).offset(offset).all()
        return food_list
    except Exception as e:
        raise e
