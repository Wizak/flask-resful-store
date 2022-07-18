from app import bc
from app import db


class _AdminValidation:
    def __init__(self, obj, data=None):
        self.obj = obj
        self.data = data


    @property
    def get_admin(self):
        admin = self._is_exist()
        return admin


    def _is_exist(self):
        admin_query = self.obj.query.filter_by(
            username=self.data['username']).one_or_none()
        return admin_query


class AdminController(_AdminValidation):
    def register(self):
        if self.data:
            admin = self._is_exist()
            if admin is None:
                pswd = bc.generate_password_hash(self.data['password']).decode('utf-8')
                admin_change = self.obj(
                    username=self.data['username'],
                    password=pswd,
                    permission=True)
                db.session.add(admin_change)
                db.session.commit()
                return True
        print('[+] WARNING: may be missed content')


    def login(self):
        if self.data:
            admin = self._is_exist()
            if admin:
                check = bc.check_password_hash(admin.password, self.data['password'])
                return all([check, self.obj.permission])
        print('[+] WARNING: may be missed content')     
    
    
    def update_account(self, username):
        admin = self.query(self.data['username'])
        admin.username = username
        db.session.commit()
        return True


    def delete_account(self, username):
        admin = self.query(username)
        db.session.delete(admin)
        db.session.commit()
        return True


    def query(self, username=None):
        if username:
            admin = self.obj.query.filter_by(username=username).one_or_none()
            return admin
        else:
            admins = self.obj.query.all()
            return admins


class StoreController:
    def __init__(self, obj, data=None):
        self.obj = obj
        self.data = data

    def _is_exist(self, data):
        sku_data = data['sku'].split('-')
        store_query = self.obj.query.filter_by(
            sku=sku_data).one_or_none()
        return store_query


    def add_product(self):
        if self.data:
            for product in self.data:
                check = self._is_exist(product)
                if check is None:
                    sku_data = product['sku'].split('-')
                    product['sku'] = sku_data
                    store = self.obj(**product)
                    db.session.add(store)
                    db.session.commit()
            return True


class TokenController:
    def __init__(self, obj, jti, created_at):
        self.obj = obj
        self.jti = jti
        self.created_at = created_at

    
    def add_to_db(self):
        token_block_list = self.obj(jti=self.jti, created_at=self.created_at)
        db.session.add(token_block_list)
        db.session.commit()
