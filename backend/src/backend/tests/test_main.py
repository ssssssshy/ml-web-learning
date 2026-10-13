import pytest
from fastapi.testclient import TestClient

from backend.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_predict_positive(client):
    response = client.post("/api/v1/predictions/", json={"text": "great movie"})

    assert response.status_code == 200
    assert response.json() == {"text": "great movie", "sentiment": "positive"}


def test_predict_empty_text(client):
    response = client.post("/api/v1/predictions/", json={"text": "   "})

    assert response.status_code == 422


@pytest.mark.parametrize(
    "text, expected",
    [
        ("great movie", "positive"),
        ("bad movie", "negative"),
        ("hello world", "neutral"),
    ],
)
def test_sentiment(client, text, expected):
    response = client.post("/api/v1/predictions/", json={"text": text})
    assert response.status_code == 200
    assert response.json()["sentiment"] == expected
