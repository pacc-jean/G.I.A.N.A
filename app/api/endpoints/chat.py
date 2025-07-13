from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.message import MessageCreate, MessageResponse
from app.models.message import Message
from app.models.session import Session as ChatSession
from datetime import datetime
from fastapi import Depends

router = APIRouter(prefix="/chat", tags=["chat"])

@router.post("/message", response_model=MessageResponse)
def create_message(message: MessageCreate, db: Session = Depends(get_db)):
    # Check if the session exists
    session = db.query(ChatSession).filter_by(session_id=message.session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found.")

    # Store user message in DB
    new_message = Message(
        session_id=message.session_id,
        role=message.role,
        content=message.content,
        timestamp=datetime.now()
    )
    db.add(new_message)
    db.commit()
    db.refresh(new_message)

    # For now, just echo the message back (until we hook up the LLM)
    return new_message
