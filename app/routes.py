from flask import jsonify
from flask import Blueprint

from app import jwt
from app import db

from app.models import TokenBlocklist
from app.models import UserTable


main_bp = Blueprint('main', __name__)


@main_bp.before_app_first_request
def db_create():
    db.create_all()


@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    token = db.session.query(TokenBlocklist.id).filter_by(jti=jti).scalar()
    return token is not None


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id_user


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return UserTable.query.filter_by(id_user=identity).one_or_none()


@jwt.expired_token_loader
def my_expired_token_callback(jwt_header, jwt_payload):
    return jsonify(code="dave", err="Token is expired"), 401