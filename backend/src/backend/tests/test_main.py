from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_predict_positive():
    response = client.post("/api/v1/predictions/", json={"text": "great movie"})

    assert response.status_code == 200
    assert response.json() == {"text": "great movie", "sentiment": "positive"}


def test_predict_empty_text():
    response = client.post("/api/v1/predictions/", json={"text": "   "})

    assert response.status_code == 422
