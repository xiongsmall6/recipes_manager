#!/user/bin/env python
# -*- coding: utf-8 -*-

"""
@File  : views.py
@desc: 蓝本中定义的程序路由
"""
from app.main import main as ma
from flask import render_template, request, jsonify
from  app.main.utils import reptile,common_utils
from app.main.model.rest_result import RestResultUtil
from app.main.model.food import Food
from app.main.model.user import User
from app.main.service import food_service, user_service
from flask import current_app
import json
import uuid
import traceback
import os

# =========== index ===========
@ma.route('/', methods=['GET', 'POST'])
def index():
    # 跳转至创建模型页
    return "success"


@ma.route('/init', methods=['GET', 'POST'])
def add_model():
    try:
        datas = reptile.reptile_food(30)
        for data in datas:
            food = Food()
            food.food_name = data['food_name']
            food.food_type = data['food_type']
            food.create_user = "admin"
            food.food_image = data['food_image']
            food.food_info = data['food_info']
            food_material = data['food_material']
            food_service.add_food(food)
            for material in food_material:
                material['food_id'] = food.id
            food_service.add_food_material(food_material)
            food_step = data['food_step']
            for step in food_step:
                step['food_id'] = food.id
            food_service.add_food_step(food_step)
        return jsonify("")
    except Exception as e:
        current_app.logger.error("添加数据失败：{0}\n{1}".format(e, traceback.format_exc()))
        result = RestResultUtil(-1, "服务异常", None)
        return jsonify(result.serialize)


@ma.route('/day', methods=['GET', 'POST'])
def food_day():
    try:
        morning = food_service.query_food_random(1)
        noon = food_service.query_food_random(2)
        night = food_service.query_food_random(3)
        return jsonify({"morning": morning, 'noon': noon, "night": night})
    except Exception as e:
        current_app.logger.error("获取首页数据失败：{0}\n{1}".format(e, traceback.format_exc()))
        result = RestResultUtil(-1, "服务异常", None)
        return jsonify(result.serialize)


@ma.route('/detail', methods=['GET', 'POST'])
def food_detail():
    try:
        food_id = request.values.get("food_id")
        food = food_service.query_food_by_id(food_id);
        food_material = food_service.query_material(food_id);
        foo_step = food_service.query_step(food_id)
        if food is None:
            return
        food = food.serialize
        food['food_material'] = [i.serialize for i in food_material]
        food['food_step'] = [j.serialize for j in foo_step]
        return jsonify(food)
    except Exception as e:
        current_app.logger.error("获取菜谱详情失败：{0}\n{1}".format(e, traceback.format_exc()))
        result = RestResultUtil(-1, "服务异常", None)
        return jsonify(result.serialize)


@ma.route('/list', methods=['GET', 'POST'])
def food_list_query():
    try:
        create_user = request.values.get("create_user")
        food_type = request.values.get("food_type")
        search = request.values.get("search")
        page = request.values.get("page")
        limit = request.values.get("limit")
        food_list = food_service.query_food_list(int(page), int(limit), create_user, food_type, search)
        if food_list is not None and len(food_list) > 0:
            food_list = [i.serialize for i in food_list]
        result = RestResultUtil(0, "请求成功", food_list)
        return jsonify(result.serialize)
    except Exception as e:
        current_app.logger.error("获取菜谱列表失败：{0}\n{1}".format(e, traceback.format_exc()))
        result = RestResultUtil(-1, "服务异常", None)
        return jsonify(result.serialize)


@ma.route('/register', methods=['GET', 'POST'])
def food_register():
    try:
        user_name = request.values.get("user_name")
        password = request.values.get("password")
        if user_name is None or user_name == "" or password is None or password == "":
            result = RestResultUtil(-2, "缺少必填参数", None)
            return jsonify(result.serialize)
        user = user_service.query_user(user_name)
        if user is not None:
            result = RestResultUtil(-3, "用户名已存在", None)
            return jsonify(result.serialize)
        user = User()
        user.user_name = user_name
        user.password = password
        user.nike_name = "帅气厨神"
        user.gender = 1;
        user.user_image = "http://"+common_utils.get_host_ip()+":8081/food/static/image/man_default.png"
        user_service.add_user(user)
        result = RestResultUtil(0, "请求成功", user.serialize)
        return jsonify(result.serialize)
    except Exception as e:
        current_app.logger.error("注册用户失败：{0}\n{1}".format(e, traceback.format_exc()))
        result = RestResultUtil(-1, "服务异常", None)
        return jsonify(result.serialize)


@ma.route('/login', methods=['GET', 'POST'])
def food_login():
    try:
        user_name = request.values.get("user_name")
        password = request.values.get("password")
        if user_name is None or user_name == "" or password is None or password == "":
            result = RestResultUtil(-2, "缺少必填参数", None)
            return jsonify(result.serialize)
        user = user_service.query_user(user_name)
        if user is None:
            result = RestResultUtil(-3, "用户名密码错误", None)
            return jsonify(result.serialize)
        if user.password == password:
            result = RestResultUtil(0, "登录成功", user.serialize)
            return jsonify(result.serialize)
        else:
            result = RestResultUtil(-3, "用户名密码错误", None)
            return jsonify(result.serialize)
    except Exception as e:
        current_app.logger.error("登录用户成功：{0}\n{1}".format(e, traceback.format_exc()))
        result = RestResultUtil(-1, "服务异常", None)
        return jsonify(result.serialize)


@ma.route('/update', methods=['GET', 'POST'])
def food_update():
    try:
        user_id = request.values.get("user_id")
        nike_name = request.values.get("nike_name")
        age = request.values.get("age")
        gender = request.values.get("gender")
        image_file = request.files.get("user_image")
        user_image = None
        if image_file is not None:
            ext = image_file.filename.rsplit('.', 1)[1]
            file_name = uuid.uuid1()
            save_path = os.path.abspath(".")
            save_file = "{0}/app/static/image/{1}.{2}".format(save_path, file_name, ext)
            image_file.save(save_file)
            user_image = "http://{0}:8081/food/static/image/{1}.{2}".format(common_utils.get_host_ip(), file_name, ext)
        else:
            if int(gender) == 1:
                user_image = "http://" + common_utils.get_host_ip() + ":8081/food/static/image/man_default.png"
            else:
                user_image = "http://" + common_utils.get_host_ip() + ":8081/food/static/image/woman_default.png"
        user = user_service.update_user(int(user_id), nike_name, user_image, age, gender)
        result = RestResultUtil(0, "请求成功", user.serialize)
        return jsonify(result.serialize)
    except Exception as e:
        current_app.logger.error("更新用户失败：{0}\n{1}".format(e, traceback.format_exc()))
        result = RestResultUtil(-1, "服务异常", None)
        return jsonify(result.serialize)


@ma.route('/upload/image', methods=['GET', 'POST'])
def upload_image():
    try:
        user_id = request.values.get("user_id")
        image_file = request.files.get("user_image")
        user_image = None
        if image_file is not None:
            file_name = image_file.filename
            save_path = os.path.abspath(".")
            save_file = "{0}/app/static/image/{1}_{2}".format(save_path, user_id, file_name)
            image_file.save(save_file)
            user_image = "http://{0}:8081/food/static/image/{1}_{2}".format(common_utils.get_host_ip(), user_id, file_name)
        result = RestResultUtil(0, "请求成功", user_image)
        return jsonify(result.serialize)
    except Exception as e:
        current_app.logger.error("上传图片失败：{0}\n{1}".format(e, traceback.format_exc()))
        result = RestResultUtil(-1, "服务异常", None)
        return jsonify(result.serialize)


@ma.route('/add', methods=['GET', 'POST'])
def food_add():
    try:
        food_json = request.values.get("food")
        data = json.loads(food_json)
        print(data)
        food = Food()
        food.food_name = data['food_name']
        food.food_type = data['food_type']
        food.create_user = data['create_user']
        food.food_image = data['food_image']
        food.food_info = data['food_info']
        food_material = data['food_material']
        food_service.add_food(food)
        for material in food_material:
            material['food_id'] = food.id
        food_service.add_food_material(food_material)
        food_step = data['food_step']
        for step in food_step:
            step['food_id'] = food.id
        food_service.add_food_step(food_step)
        result = RestResultUtil(0, "请求成功", None)
        return jsonify(result.serialize)
    except Exception as e:
        current_app.logger.error("添加美食成功失败：{0}\n{1}".format(e, traceback.format_exc()))
        result = RestResultUtil(-1, "服务异常", None)
        return jsonify(result.serialize)

