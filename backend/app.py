from flask import Flask
from config import Config
from extensions import db  # Import db from extensions.py
from passlib.hash import argon2  # or use bcrypt

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize extensions
    db.init_app(app)
    
    # Import models
    #from models import User

    @app.route('/')
    def index():
        

        # Hash a password for the first time
        #hashed_password = argon2.hash("pass")
        #print (hashed_password)
        return "Flask server is running!"

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
