from flask import make_response, render_template
from flask_restful import Resource, reqparse
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token


class Login(Resource):
    realpw = 'dango'
    
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('login.html'), 200, headers)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('password', type=str)
        parser.add_argument('userId', type=str)
        user = parser.parse_args()['userId']
        password = parser.parse_args()['password']

        resp = {}
        if password == self.realpw:
            resp['success'] = 1
            resp['token'] = create_access_token(identity=user)
            resp['refreshToken'] = create_refresh_token(identity=user)
            return resp

        resp['success'] = 0
        resp['message'] = 'wrong password'
        return resp


