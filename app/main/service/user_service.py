from app.main.model.user import User
from app import db
from sqlalchemy import text


def add_user(user):
    """ 添加用户"""
    try:
        db.session.add(user)
        db.session.commit()
        return user
    except Exception as e:
        db.session.rollback()
        raise e


def update_user(user_id, nike_name, user_image, age, gender):
    """修改用户"""
    try:
        user = db.session.query(User).filter(User.id == user_id).first()
        if user is not None:
            if nike_name is not None:
                user.nike_name = nike_name
            if user_image is not None:
                user.user_image = user_image
            if age is not None:
                user.age = age
            if gender is not None:
                user.gender = gender
        db.session.commit()
        return user
    except Exception as e:
        db.session.rollback()
        raise e


def query_user(user_name):
    """修改用户"""
    try:
        user = db.session.query(User).filter(User.user_name == user_name).first()
        return user
    except Exception as e:
        db.session.rollback()
        raise e


