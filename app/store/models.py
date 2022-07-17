from app.models import StoreTable, CartTable


class Store(StoreTable):
    def __init__(self, **kwds):
        self.name = kwds['name']
        self.description = kwds['description']
        self.sku = kwds['sku']


    def dict_to_json(self):
        return {
            'name': self.name,
            'description': self.description,
            'sku': '-'.join(self.sku)
        }


class Cart(CartTable):
    def __init__(self, **kwds):
        self.skus = kwds['skus']
    