from flask import jsonify
from flask import request
from flask import json

from flask_restful import Resource
from flask_jwt_extended import current_user, jwt_required

from app.user.models import User
from .models import Store
from .models import Cart

from app.user.controllers import UserController
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
        control = StoreController(Store)
        product_query = control.get_products(product)
        if product_query:
            return jsonify(product_query.dict_to_json())
        return jsonify(msg='Store is empty')


@store_api.resource('/cart')
class CartShow(Resource):
    @jwt_required()
    def get(self):
        control_cart = CartController(Cart)
        check = control_cart.get_products()
        if check:
            cart = Cart.query.filter_by(user_id=current_user.id_user).all()
            products = []
            for p in cart:
                product = Store.query.filter_by(id_product=p.store_id).one_or_none()
                products.append(product.dict_to_json())
            if products:
                return jsonify(products)
            return jsonify(msg='Cart is empty')
        return jsonify(msg='Cart is empty')


@store_api.resource('/cart/<product>')
class CartModify(Resource):
    @jwt_required()
    def post(self, product):
        control_store = StoreController(Store)
        control_user = UserController(User)

        user = control_user.query(current_user.username)
        product = control_store.get_products(product)

        if product is None:
            return jsonify(msg='Product name is invalid')

        data = dict(product=product, user=user)
        control_cart = CartController(Cart, data)
        check = control_cart.add_to_cart()

        if check:
            return jsonify(msg='Successful adding product ot cart')
        return jsonify(msg='Product is not exist or/and is already exist in a cart')


    @jwt_required()
    def delete(self, product):
        control_store = StoreController(Store)
        control_user = UserController(User)

        user = control_user.query(current_user.username)
        product = control_store.get_products(product)

        if product is None:
            return jsonify(msg='Product name is invalid')

        data = dict(product=product, user=user)
        control_cart = CartController(Cart, data)
        check = control_cart.delete_from_cart()

        if check:
            return jsonify(msg='Successful delete product from cart')
        return jsonify(msg='Product is not exist or/and is already exist in a cart')
