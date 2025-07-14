from app import create_app
from app.core.extensions import db
from app.models import *

app = create_app()

with app.app_context():
    db.create_all()
    print("✅ Database initialized.")
