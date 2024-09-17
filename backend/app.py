from flask import Flask
from config import Config
from extensions import db  # Import db from extensions.py

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize extensions
    db.init_app(app)
    
    # Import models
    from models import User

    @app.route('/')
    def index():
        return "Flask server is running with password encryption!"

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
