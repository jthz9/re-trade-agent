from fastapi import FastAPI
from .core.config import settings
from backend.app.models import Base # Import Base from models package
from backend.app.db.database import engine # Import engine

app = FastAPI(title=settings.APP_NAME)


@app.on_event("startup")
async def startup_event():
    print("Application startup: Initializing database tables...")
    Base.metadata.create_all(bind=engine) # Create tables
    print("Database table initialization complete.")


@app.get("/")
async def read_root():
    return {"message": f"Welcome to {settings.APP_NAME}"}
