from datetime import datetime, timezone
from app.core.extensions import db

class Message(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String, db.ForeignKey("sessions.id"), nullable=False)
    role = db.Column(db.String, nullable=False)  # 'user' or 'giana'
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
