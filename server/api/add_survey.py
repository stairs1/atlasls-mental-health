from flask_restful import Resource
from server.app import db

class AddSurvey(Resource):
    def put(self):
        data=json.loads(request.form['data'])
        
        return db.surveys.insert_one(data).acknowledged
        
