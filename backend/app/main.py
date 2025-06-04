from fastapi import FastAPI
from .core.config import settings
from app.db import sqlite_utils # Database utilities

app = FastAPI(title=settings.APP_NAME)


@app.on_event("startup")
async def startup_event():
    print("Application startup: Initializing database...")
    sqlite_utils.initialize_db()
    print("Database initialization complete.")


@app.get("/")
async def read_root():
    return {"message": f"Welcome to {settings.APP_NAME}"}
