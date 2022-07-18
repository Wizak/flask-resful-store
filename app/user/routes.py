from flask import jsonify
from flask import request
from flask import json
from flask_restful import Resource

from flask_jwt_extended import jwt_required
from flask_jwt_extended import create_access_token
from flask_jwt_extended import current_user
from flask_jwt_extended import get_jwt

from datetime import datetime
from datetime import timezone

from .models import User
from app.models import TokenBlocklist

from .controllers import UserController
from .controllers import TokenController

from . import user_api
from . import users_api

from app import db


@user_api.resource('/')
class UserCreate(Resource):
    def post(self):
        data = json.loads(request.data)
        if 'username' in data and 'password' in data:
            control = UserController(User, data)
            check = control.register()
            if check:
                return jsonify(msg='successful registration')
            return jsonify(msg='username is exist')
        return jsonify(msg='Bad fields')


@user_api.resource('/login')
class UserLogin(Resource):
    def post(self):
        data = json.loads(request.data)
        control = UserController(User, data)
        check = control.login()
        if check:
            access_token = create_access_token(identity=control.get_user)
            return jsonify(access_token=access_token)
        return jsonify(msg='username or password is invalid')


@user_api.resource('/logout')
class UserLogout(Resource):
    @jwt_required()
    def delete(self):
        jti = get_jwt()["jti"]
        now = datetime.now(timezone.utc)
        control = TokenController(TokenBlocklist, jti, now)
        control.add_to_db()
        return jsonify(msg="JWT revoked")


@user_api.resource('/account')
class UserAccount(Resource):
    @jwt_required()
    def get(self):
        if current_user:
            control = UserController(User)
            user = control.query(current_user.username)
            if user:
                return jsonify(user.dict_to_json())
            return jsonify(msg='user invalid')
        return jsonify(msg='user is not loggined')


    @jwt_required()
    def put(self):
        if current_user:
            data = json.loads(request.data)
            control = UserController(User, {'username': current_user.username})
            check = control.update_account(data)
            if check:
                return jsonify(msg='Succesful updating account')
            return jsonify(msg='Invalid data')
        return jsonify(msg='user is not loggined')
    

    @jwt_required()
    def delete(self):
        if current_user:
            control = UserController(User)
            check = control.delete_account(current_user.username)
            if check:
                return jsonify(msg='Successful delete user')
            return jsonify(msg='Invalid data')
        return jsonify(msg='user is not loggined')



@users_api.resource('/')
class UsersShow(Resource):
    @jwt_required()
    def get(self):
        if current_user:
            control = UserController(User)
            users = control.query()
            if users:
                users_show = [
                    {'username': user.username}
                    for user in users
                ]
                return jsonify(users_show)
            return jsonify(msg='users is empty')
        return jsonify(msg='user is not loggined')


@users_api.resource('/<username>')
class UserShow(Resource):
    @jwt_required()
    def get(self, username):
        if current_user:
            control = UserController(User)
            user = control.query(username)
            if user:
                return jsonify(username=user.username, avatar=user.bin_to_json(user.avatar))
            return jsonify(msg='username is invalid')
        return jsonify(msg='user is not loggined')
