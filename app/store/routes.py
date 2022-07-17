from flask import jsonify
from flask import request
from flask import json

from flask_restful import Resource
from flask_jwt_extended import current_user, jwt_required

from app.user.models import User

from .models import Store
from .models import Cart

from .controllers import StoreController
from .controllers import CartController

from . import store_api
from app import jwt


@store_api.resource('/')
class StoreShow(Resource):
    def get(self):
        control = StoreController(Store)
        products = control.get_products()
        if products:
            product = [p.dict_to_json() for p in products]
            return jsonify(product)
        return jsonify(msg='Store is empty')


@store_api.resource('/<product>')
class ProductShow(Resource):
    def get(self, product):
        pass


@store_api.resource('/cart')
class CartShow(Resource):
    @jwt_required()
    def get(self):
        pass


@store_api.resource('/cart/<product>')
class CartModify(Resource):
    @jwt_required()
    def post(self):
        pass


    @jwt_required()
    def put(self, product):
        pass


    @jwt_required()
    def delete(self, product):
        pass
