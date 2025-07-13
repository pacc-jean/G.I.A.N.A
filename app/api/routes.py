from fastapi import APIRouter
from app.api.endpoints import chat

router = APIRouter()
router.include_router(chat.router)

@router.get("/")
async def root():
    return {"message": "G.I.A.N.A system online. Awaiting commands."}
