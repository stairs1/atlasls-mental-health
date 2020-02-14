from flask import Flask, request, render_template, redirect, url_for, make_response
from flask_restful import Resource, Api, fields, marshal_with
from flask_jwt_extended import JWTManager
from pymongo import MongoClient
import json
from server.settings import Settings
import os


app = Flask(__name__)
app.config.from_object(Settings)
app._static_folder = os.path.abspath("templates/static/")
api = Api(app)
jwt = JWTManager(app)

client = MongoClient()
db = client.surveydb

from server.api.login import Login
from server.api.data import Data
from server.api.add_user import AddUser
from server.api.add_survey import AddSurvey
from server.api.home import Home

api.add_resource(AddUser, '/adduser')
api.add_resource(AddSurvey, '/addsurvey')
api.add_resource(Login, '/')
api.add_resource(Data, '/data')
api.add_resource(Home, '/home')

if __name__ == '__main__':
    app.run(debug=True)

