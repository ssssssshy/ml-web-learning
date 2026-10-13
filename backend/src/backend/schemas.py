from pydantic import BaseModel, field_validator


class Message(BaseModel):
    text: str

    @field_validator("text")
    @classmethod
    def validate_text(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("Text cannot be empty")

        return value


class PredictionResponse(BaseModel):
    text: str
    sentiment: str
