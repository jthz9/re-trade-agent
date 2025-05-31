from fastapi import FastAPI
from .core.config import settings

app = FastAPI(title=settings.APP_NAME)


@app.get("/")
async def read_root():
    return {"message": f"Welcome to {settings.APP_NAME}"}
