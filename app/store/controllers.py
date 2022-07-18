from app import db


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
    def __init__(self, obj, data=None):
        self.obj = obj
        self.data = data


    def get_products(self, product_name=None):
        if product_name:
            product = self.obj.query.filter_by(name=product_name).one_or_none()
            return product
        else:
            products = self.obj.query.all()
            return products


    def add_to_cart(self):
        if self.data:
            user_id = self.data['user'].id_user
            product_id = self.data['product'].id_product
            check_uc = self.obj.query.filter_by(user_id=user_id).all()
            for c in check_uc:
                if c.store_id == product_id:
                    return False
            cart_product = self.obj(user_id=user_id, store_id=product_id)
            db.session.add(cart_product)
            db.session.commit()
            return True
    

    def delete_from_cart(self):
        if self.data:
            user_id = self.data['user'].id_user
            product_id = self.data['product'].id_product
            check_uc = self.obj.query.filter_by(user_id=user_id).all()
            if check_uc:
                for c in check_uc:
                    if c.store_id == product_id:
                        db.session.delete(c)
                        db.session.commit()
                        return True
