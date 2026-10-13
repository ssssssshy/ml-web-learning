from fastapi import FastAPI

from backend.config import settings
from backend.routers.predictions import router as predictions_router

app = FastAPI(title=settings.app_name, debug=settings.debug)

app.include_router(predictions_router)


@app.get("/")
def analyze_api():
    return {"message": "Review Intelligence API"}


@app.get("/health")
def get_status():
    return {"status": "ok"}
