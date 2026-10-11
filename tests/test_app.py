from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_predict_success():
    response = client.post(
        "/predict", json={"text": "What a great MLOps lecture, I am very satisfied"}
    )
    assert response.status_code == 200
    assert response.json()["prediction"] in ["positive", "neutral", "negative"]


def test_predict_empty_text():
    response = client.post("/predict", json={"text": ""})
    assert response.status_code == 422


def test_predict_invalid_payload():
    response = client.post("/predict", json={"invalid_key": "some text"})
    assert response.status_code == 422
