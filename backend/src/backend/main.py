from fastapi import FastAPI

from backend.schemas import Message, PredictionResponse
from backend.services import analyze_sentiment

app = FastAPI()


@app.get("/")
def analyze_api():
    return {"message": "Review Intelligence API"}


@app.get("/health")
def get_status():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictionResponse)
def predict(message: Message):
    sentiment = analyze_sentiment(message.text)

    return {
        "text": message.text,
        "sentiment": sentiment,
    }
