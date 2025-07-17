from flask import Flask
from flask_cors import CORS
from app.routes.main import main_bp
from app.core.config import Config
from app.core.extensions import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    CORS(app)

    app.register_blueprint(main_bp)

    return app
