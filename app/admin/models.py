from app.models import UserTable, StoreTable
from base64 import b64encode


class Admin(UserTable):
    def __init__(self, **kwds):
        self.username = kwds['username']
        self.password = kwds['password']
        if 'permission' in kwds:
            self.permission = kwds['permission']


    def bin_to_json(self, element):
        return b64encode(element).decode("utf8")


    def json_to_bin(self, element):
        return element.encode('utf-8')


    def dict_to_json(self):
        return {
            'username': self.username
        }


class Store(StoreTable):
    def __init__(self, **kwds):
        self.name = kwds['name']
        self.sku = kwds['sku']
        self.description = kwds['description']
    
    
    def dict_to_json(self):
        return {
            'name': self.name,
            'sku': self.sku,
            'description': self.description
        }
