from flask import Flask, request, render_template, redirect, url_for
from flask_restful import Resource, Api, fields, marshal_with
from settings import Settings
from login import LoginForm
from pymongo import MongoClient
import json

app = Flask(__name__)
app.config.from_object(Settings)
api = Api(app)

client = MongoClient()
db = client.surveydb

users = []
surveys = []

# data_fields = {
#         'user': fields.String,
#         'surveys': fields.Listkkk

class AddUser(Resource):
    def put(self):
        import pdb; pdb.set_trace()
        uid = request.form['id']
        return db.users.insert_one({'id': uid}).acknowledged

class AddSurvey(Resource):
    def put(self):
        data=json.loads(request.form['data'])
        
        return db.surveys.insert_one(data).acknowledged
        
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

class WebPage(Resource):
    def get(self):
        return render_template('static.html')

@app.route('/home')
def home():
    return render_template('static.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('login.html', title='Sign in please', form=form)

api.add_resource(AddUser, '/adduser')
api.add_resource(AddSurvey, '/addsurvey')
api.add_resource(Data, '/data')
api.add_resource(WebPage, '/home2')

if __name__ == '__main__':
    app.run(debug=True)

