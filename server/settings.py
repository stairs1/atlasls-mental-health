import os

class Settings(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'bibbity-boppity'
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'several pennies'
    JWT_TOKEN_LOCATION = ['headers', 'cookies']
    PROPAGATE_EXCEPTIONS = True
    WTF_CSRF_ENABLED = False

