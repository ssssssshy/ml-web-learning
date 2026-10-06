from fastapi import FastAPI

from backend.routers.predictions import router as predictions_router

app = FastAPI()

app.include_router(predictions_router)


@app.get("/")
def analyze_api():
    return {"message": "Review Intelligence API"}


@app.get("/health")
def get_status():
    return {"status": "ok"}
