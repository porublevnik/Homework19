from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from implemented import user_service

user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):
    def get(self):
        data = user_service.get_all()
        return UserSchema(many=True).dump(data), 200

    def post(self):
        data = request.json
        user_service.create(data)
        return "User added", 201


@user_ns.route('/<int:uid>')
class UserView(Resource):
    def get(self, uid):
        user = user_service.get_one_by_id(uid)
        if user is None:
            return 'User not found', 404
        return UserSchema().dump(user), 200

    def put(self, uid):
        data = request.json
        data['id'] = uid
        if user_service.get_one_by_id(uid) is None:
            return 'User not found', 404
        user_service.update(data)
        return "User updated", 201

    def delete(self, uid):
        if user_service.get_one_by_id(uid) is None:
            return 'User not found', 404
        user_service.delete(uid)
        return "User deleted", 201