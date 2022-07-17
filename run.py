from app import create_app
from config import PostgresSqlConfig


if __name__ == '__main__':
    store_app = create_app(PostgresSqlConfig)
    store_app.run(debug=True)
