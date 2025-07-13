from pydantic import BaseModel, Field
from datetime import datetime
from typing import Literal


class MessageCreate(BaseModel):
    session_id: str = Field(..., description="The session this message belongs to")
    role: Literal["user", "giana"] = Field(..., description="Who sent the message")
    content: str = Field(..., min_length=1, description="The content of the message")


class MessageResponse(BaseModel):
    id: int
    session_id: str
    role: Literal["user", "giana"]
    content: str
    timestamp: datetime
