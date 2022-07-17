from flask import Blueprint
from flask_restful import Api


store_bp = Blueprint('store', __name__, url_prefix='/store')
store_api = Api(store_bp)


from . import routes
