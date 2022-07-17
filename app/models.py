from app import db
from app.utils import Avatar

from sqlalchemy.dialects.postgresql import UUID

import uuid


class UserTable(db.Model):
    __tablename__ = 'users'

    id_user = db.Column(
        'id',
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True)
    username = db.Column(db.String(20), nullable=False, unique=True, index=True)
    password = db.Column(db.Text, nullable=False)
    permission = db.Column(db.Boolean, default=False)
    avatar = db.Column(db.LargeBinary, default=Avatar.get_from_file())
    cart = db.relationship('CartTable', backref='user', lazy=True)


class StoreTable(db.Model):
    __tablename__ = 'products'

    id_product = db.Column(
        'id',
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True)
    name = db.Column(db.String(20), nullable=False, unique=True, index=True)
    description = db.Column(db.Text, default='Some product...')
    sku = db.Column(db.ARRAY(db.String), nullable=False, index=True)


class CartTable(db.Model):
    __tablename__ = 'carts'

    id_cart = db.Column(
        'id',
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True)
    skus = db.Column(db.ARRAY(db.String), nullable=False, index=True)
    user_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey('users.id'),
        default=uuid.uuid4,
        index=True)


class TokenBlocklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False, index=True)
    created_at = db.Column(db.DateTime, nullable=False)
