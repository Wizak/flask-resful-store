from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS


db = SQLAlchemy()
bc = Bcrypt()
jwt = JWTManager()

from app import routes
from app.models import UserTable
from app.models import TokenBlocklist
from app.models import StoreTable
from app.models import CartTable


def create_app(config_settings):
    app = Flask(__name__)
    app.config.from_object(config_settings)

    CORS(app)
    db.init_app(app)
    bc.init_app(app)
    jwt.init_app(app)


    @app.before_first_request
    def db_create():
        db.create_all()


    from app.user import user_bp
    app.register_blueprint(user_bp)

    from app.user import users_bp
    app.register_blueprint(users_bp)

    from app.store import store_bp
    app.register_blueprint(store_bp)

    from app.admin import admin_bp
    app.register_blueprint(admin_bp)

    from app.docs import swaggerui_bp
    app.register_blueprint(swaggerui_bp)


    return app
