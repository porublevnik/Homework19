import base64

from dao.user_dao import UserDAO
import hashlib
import hmac
from helpers.constants import *


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one_by_id(self, uid):
        return self.dao.get_one_by_id(uid)

    def get_one_by_username(self, username):
        return self.dao.get_one_by_username(username)

    def get_all(self):
        return self.dao.get_all()

    def create(self, user_d):
        user_d['password'] = self.get_hash(user_d['password'])
        return self.dao.create(user_d)

    def update(self, user_d):
        self.dao.update(user_d)
        return self.dao

    def delete(self, uid):
        self.dao.delete(uid)

    def get_hash(self, password):
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return base64.b64encode(hash_digest)

    def check_password(self, hash, password):
        decode_digest = base64.b64decode(hash)
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return hmac.compare_digest(hash_digest, decode_digest)

    # def get_hash(self, password):
    #     hash_digest = hashlib.pbkdf2_hmac(
    #         'sha256',
    #         password.encode('utf-8'),
    #         PWD_HASH_SALT,
    #         PWD_HASH_ITERATIONS
    #     )
    #     return hash_digest
    #
    # def check_password(self, password, input_password):
    #     password_hash = self.get_hash(password)
    #     input_password_hash = self.get_hash(input_password)
    #
    #     return hmac.compare_digest(password_hash, input_password_hash)