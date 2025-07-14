import uuid
from datetime import datetime, timezone
from app.core.extensions import db

class Session(db.Model):
    __tablename__ = "sessions"

    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String, nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
