from flask import make_response, render_template
from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class MyForm(FlaskForm):
    name = StringField('Add user:', validators=[DataRequired()])


class Home(Resource):

    @jwt_required
    def get(self):
        form = MyForm()
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('home.html', form=form), 200, headers)

    @jwt_required
    def post(self):
        import pdb; pdb.set_trace()
        form = MyForm()
        headers = {'Content-Type': 'text/html'}
        if form.validate():
            return make_response(render_template('static.html'), 200, headers)
        else:
            return make_response(render_template('home.html', form=form), 200, headers)

