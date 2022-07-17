from datetime import timedelta


class Config:
    ADMIN_SECRET_KEY = 'adminsecretkey'
    JWT_SECRET_KEY = 'SuperSecretKey'
    JWT_ALGORITHM = 'HS256'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class MySqlConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://{0}:{1}@{2}/{3}'.format(
        'Wizak',
        'admin',
        'http://127.0.0.1/3306',
        'pet_store')

class PostgresSqlConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{0}:{1}@{2}/{3}'.format(
        'postgres',
        'admin',
        '127.0.0.1:5432',
        'store')
