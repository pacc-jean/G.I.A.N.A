import os
from pathlib import Path
from dotenv import load_dotenv

# Project root: adjust if your structure differs
BASE_DIR = Path(__file__).resolve().parent.parent.parent  # app/core -> app -> project root

# Load .env (if present)
load_dotenv(BASE_DIR / ".env")

class Config:
    # DB
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL") or f"sqlite:///{BASE_DIR / 'giana.db'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Ollama / LLM
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "mistral")
    OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    # seconds; env always str, so cast
    OLLAMA_TIMEOUT = float(os.getenv("OLLAMA_TIMEOUT", "60"))
