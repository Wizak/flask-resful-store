from flask import jsonify
from flask import request
from flask import json
from flask import current_app

from flask_restful import Resource

from flask_jwt_extended import jwt_required
from flask_jwt_extended import create_access_token
from flask_jwt_extended import current_user
from flask_jwt_extended import get_jwt

from .models import Admin
from .models import Store
from app.models import TokenBlocklist

from .controllers import AdminController
from .controllers import StoreController
from .controllers import TokenController

from . import admin_api

from datetime import datetime
from datetime import timezone


@admin_api.resource('/login')
class AdminLogin(Resource):
    def post(self):
        data = json.loads(request.data)
        control = AdminController(Admin, data)
        check = control.login()
        if check:
            access_token = create_access_token(identity=control.get_admin)
            return jsonify(access_token=access_token)
        return jsonify(msg='username or password is invalid')


@admin_api.resource('/logout')
class AdminLogout(Resource):
    @jwt_required()
    def delete(self):
        jti = get_jwt()["jti"]
        now = datetime.now(timezone.utc)
        control = TokenController(TokenBlocklist, jti, now)
        control.add_to_db()
        return jsonify(msg="JWT revoked")


@admin_api.resource('/account')
class AdminAccount(Resource):
    @jwt_required()
    def get(self):
        if current_user:
            control = AdminController(Admin)
            user = control.query(current_user.username)
            if user:
                return jsonify(user.dict_to_json())
            return jsonify(msg='user invalid')
        return jsonify(msg='user is not loggined')


    @jwt_required()
    def put(self):
        if current_user:
            data = json.loads(request.data)
            control = AdminController(Admin, {'username': current_user.username})
            check = control.update_account(data['username'])
            if check:
                return jsonify(msg='Succesful updating account')
            return jsonify(msg='Invalid data')
        return jsonify(msg='user is not loggined')
    

    @jwt_required()
    def delete(self):
        if current_user:
            control = AdminController(Admin)
            check = control.delete_account(current_user.username)
            if check:
                return jsonify(msg='Successful delete user')
            return jsonify(msg='Invalid data')
        return jsonify(msg='user is not loggined')



@admin_api.resource('/')
class AdminsShow(Resource):
    @jwt_required()
    def get(self):
        if current_user:
            control = AdminController(Admin)
            users = control.query()
            if users:
                users_show = [
                    {'username': user.username}
                    for user in users
                ]
                return jsonify(users_show)
            return jsonify(msg='users is empty')
        return jsonify(msg='user is not loggined')


@admin_api.resource('/product')
class AdminProduct(Resource):
    @jwt_required()
    def post(self):
            data = json.loads(request.data)
            control = StoreController(Store, data)
            check = control.add_product()
            if check:
                return jsonify(msg='successful adding')
            return jsonify(msg='request products is empty')


@admin_api.resource('/<secret>')
class AdminCreate(Resource):
    def post(self, secret):
        if secret == current_app.config['ADMIN_SECRET_KEY']:
            data = json.loads(request.data)
            if 'username' in data and 'password' in data:
                control = AdminController(Admin, data)
                check = control.register()
                if check:
                    return jsonify(msg='successful registration')
                return jsonify(msg='username is exist')
            return jsonify(msg='bad fields')
        return jsonify(msg='incorrect admin key')
