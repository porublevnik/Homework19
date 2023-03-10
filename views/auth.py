from flask import request
from flask_restx import Resource, Namespace

from implemented import auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):

    def post(self):
        data = request.json

        username = data.get('username')
        password = data.get('password')

        if None in [username, password]:
            return 401

        tokens = auth_service.generate_token(username, password)
        return tokens, 201

    def put(self):
        data = request.json
        token = data.get('refresh_token')

        if token is None:
            return 401

        tokens = auth_service.refresh_token(token)
        return tokens, 201