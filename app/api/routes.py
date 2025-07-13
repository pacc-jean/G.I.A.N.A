from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "G.I.A.N.A system online. Awaiting commands."}
