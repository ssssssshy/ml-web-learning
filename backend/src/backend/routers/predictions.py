from fastapi import APIRouter

from backend.schemas import Message, PredictionResponse
from backend.services import analyze_sentiment

router = APIRouter(
    prefix="/api/v1/predictions",
    tags=["predictions"],
)


@router.post("/", response_model=PredictionResponse)
def predict(message: Message):
    sentiment = analyze_sentiment(message.text)

    return {
        "text": message.text,
        "sentiment": sentiment,
    }
