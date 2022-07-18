from app.models import StoreTable, CartTable


class Store(StoreTable):
    def __init__(self, **kwds):
        self.name = kwds['name']
        self.sku = kwds['sku']
        if 'description' in kwds:
            self.description = kwds['description']       


    def dict_to_json(self):
        return {
            'name': self.name,
            'description': self.description,
            'sku': '-'.join(self.sku)
        }


class Cart(CartTable):
    def __init__(self, **kwds):
        self.user_id = kwds['user_id']
        self.store_id = kwds['store_id']
    