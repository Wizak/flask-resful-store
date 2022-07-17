from flask import Blueprint
from flask_restful import Api


user_bp = Blueprint('user', __name__, url_prefix='/user')
users_bp = Blueprint('users', __name__, url_prefix='/users')

user_api = Api(user_bp)
users_api = Api(users_bp)


from . import routes
