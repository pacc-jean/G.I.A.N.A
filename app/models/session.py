from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime, timezone

Base = declarative_base()

class Session(Base):
    __tablename__ = "sessions"

    session_id = Column(String, primary_key=True, index=True)
    user_name = Column(String, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    messages = relationship("Message", back_populates="session")
