class Avatar:
    @classmethod
    def get_from_file(cls, path='app/static/avatar.png'):
        with open(path, 'rb') as f:
            bimg = f.read()
        return bimg