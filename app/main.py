from fastapi import FastAPI
from app.api.routes import router as api_router

app = FastAPI(
    title="G.I.A.N.A",
    description="General Interface for AI Navigation and Assistance",
    version="0.1.0"
)

app.include_router(api_router)
