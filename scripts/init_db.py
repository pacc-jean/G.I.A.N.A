from app.core.database import engine
from app.models.base import Base

# Dynamically import models for side effects (table registration)
__import__("app.models.message")
__import__("app.models.session")

def init_db():
    print("📦 Initializing database...")
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created successfully.")

if __name__ == "__main__":
    init_db()
