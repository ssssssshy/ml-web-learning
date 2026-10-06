from fastapi import FastAPI
from pydantic import BaseModel, field_validator

app = FastAPI()


class Message(BaseModel):
    text: str


class PredictionResponse(BaseModel):
    text: str
    sentiment: str

    @field_validator("text")
    @classmethod
    def validate_text(cls, value: str):
        value = value.strip()

        if not value:
            raise ValueError("Text cannot be empty")

        return value


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


def analyze_sentiment(text: str) -> str:
    text = text.lower()
    words = text.split()
    positive_words = {"good", "great", "excellent", "love"}
    negative_words = {"bad", "terrible", "awful", "hate"}

    for word in words:
        word = word.strip(".,!?;:")
        if word in positive_words:
            return "positive"
        elif word in negative_words:
            return "negative"

    return "neutral"
