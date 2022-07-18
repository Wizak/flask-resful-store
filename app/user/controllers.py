from app import bc
from app import db


class _UserValidation:
    def __init__(self, obj, data=None):
        self.obj = obj
        self.data = data


    @property
    def get_user(self):
        user = self._is_exist()
        return user


    def _is_exist(self):
        user_query = self.obj.query.filter_by(
            username=self.data['username']).one_or_none()
        return user_query


class UserController(_UserValidation):
    def register(self):
        if self.data:
            user = self._is_exist()
            if user is None:
                pswd = bc.generate_password_hash(self.data['password']).decode('utf-8')
                user = self.obj(
                    username=self.data['username'],
                    password=pswd)
                db.session.add(user)
                db.session.commit()
                return True
        print('[+] WARNING: may be missed content')

    
    def login(self):
        if self.data:
            user = self._is_exist()
            if user:
                check = bc.check_password_hash(user.password, self.data['password'])
                return check
        print('[+] WARNING: may be missed content')
    

    def update_account(self, upd_data):
        if self.data:
            user = self._is_exist()
            if user:
                if 'username' in upd_data:
                    user.username = upd_data['username']
                if 'password' in upd_data:
                    pswd = bc.generate_password_hash(upd_data['password']).decode('utf-8')
                    user.password = pswd
                if 'avatar' in upd_data:
                    avt = self.obj.json_to_bin(upd_data['avatar'])
                    user.avatar = avt
                db.session.commit()
                return True
        print('[+] WARNING: may be missed content')

    
    def delete_account(self, username):
        user = self.query(username)
        db.session.delete(user)
        db.session.commit()
        return True


    def query(self, username=None):
        if username:
            user = self.obj.query.filter_by(username=username).one_or_none()
            return user
        else:
            users = self.obj.query.all()
            return users


class TokenController:
    def __init__(self, obj, jti, created_at):
        self.obj = obj
        self.jti = jti
        self.created_at = created_at

    
    def add_to_db(self):
        token_block_list = self.obj(jti=self.jti, created_at=self.created_at)
        db.session.add(token_block_list)
        db.session.commit()
