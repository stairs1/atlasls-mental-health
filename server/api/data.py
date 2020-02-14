from flask_restful import Resource
from server.app import db

class Data(Resource):
    def get(self):
        users = [user['id'] for user in db.users.find()]
        surveys = [
                {
                    'user': details['user'],
                    'survey': details['survey']
                } for details in db.surveys.find()
        ]
        return {'users': users, 'surveys':surveys}

