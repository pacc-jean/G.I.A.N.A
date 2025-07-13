from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="G.I.A.N.A",
    description="General Interface for AI Navigation and Assistance",
    version="0.1.0"
)

# CORS config — allows your portfolio frontend to access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can lock this down later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "G.I.A.N.A system online. Awaiting commands."}
