import os

class Config(object):
    SECRET_KEY = '123'  # Replace with a secure key
    # Ensure the database is stored in the instance folder (not root)
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_DIR, "database.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
