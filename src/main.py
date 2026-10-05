from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class PredictionRequest(BaseModel):
    text: str


@app.get("/")
def msg():
    return {"message": "hello"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predreq(request: PredictionRequest):
    return {"prediction": "positive"}
