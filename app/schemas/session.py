from pydantic import BaseModel, Field
from datetime import datetime


class SessionInitRequest(BaseModel):
    username: str = Field(..., min_length=1, description="The user's name to start or resume the session")


class SessionInitResponse(BaseModel):
    session_id: str
    message: str
    created_at: datetime
    resumed: bool  # True if existing session was found, False if new one created
