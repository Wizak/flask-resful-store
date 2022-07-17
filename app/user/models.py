from app.models import UserTable
from base64 import b64encode
from app import bc


class User(UserTable):
    def __init__(self, **kwds):
        self.username = kwds['username']
        self.password = kwds['password']
        if 'avatar' in kwds:
            self.avatar = kwds['avatar']


    def bin_to_json(self, element):
        return b64encode(element).decode("utf8")


    def json_to_bin(self, element):
        return element.encode('utf-8')


    def dict_to_json(self):
        return {
            'username': self.username,
            'avatar': self.bin_to_json(self.avatar)
        }
    