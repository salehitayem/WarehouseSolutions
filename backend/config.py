class Config(object):
    SECRET_KEY = '123'  # Replace with a secure key
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
