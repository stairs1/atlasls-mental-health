from flask_restful import Resource
from server.app import db

class AddUser(Resource):
    def put(self):
        uid = request.form['id']
        return db.users.insert_one({'id': uid}).acknowledged

