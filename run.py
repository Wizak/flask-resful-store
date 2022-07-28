from app import create_app


if __name__ == '__main__':
    store_app = create_app()
    store_app.run(debug=True)
