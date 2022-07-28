from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from flask import Flask
from flask import Blueprint

from app.config import PostgresSqlConfig


db = SQLAlchemy()
bc = Bcrypt()
jwt = JWTManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(PostgresSqlConfig)

    CORS(app)
    db.init_app(app)
    bc.init_app(app)
    jwt.init_app(app)

    app_bp = Blueprint('app_bp', __name__, url_prefix='/api/v1')

    from app import routes
    app_bp.register_blueprint(routes.main_bp)

    from app.user import user_bp
    app_bp.register_blueprint(user_bp)

    from app.user import users_bp
    app_bp.register_blueprint(users_bp)

    from app.store import store_bp
    app_bp.register_blueprint(store_bp)

    from app.admin import admin_bp
    app_bp.register_blueprint(admin_bp)

    from app.docs import swaggerui_bp
    app.register_blueprint(swaggerui_bp)

    app.register_blueprint(app_bp)

    return app
