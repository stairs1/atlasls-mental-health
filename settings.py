import os

class Settings(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'bibbity-boppity'
