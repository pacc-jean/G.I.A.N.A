from flask import Flask
from flask_cors import CORS
from app.routes.main import main_bp

def create_app():
    app = Flask(__name__)

    # Enable CORS for all origins (adjust for prod)
    CORS(app)

    # Register Blueprints
    app.register_blueprint(main_bp)

    return app
