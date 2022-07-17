class StoreController:
    def __init__(self, obj):
        self.obj = obj
    

    def get_products(self, product_name=None):
        if product_name:
            product = self.obj.query.filter_by(name=product_name).one_or_none()
            return product
        else:
            products = self.obj.query.all()
            return products
        


class CartController:
    pass