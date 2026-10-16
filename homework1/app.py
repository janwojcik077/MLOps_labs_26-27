from api.models.iris import PredictRequest, PredictResponse
from fastapi import FastAPI, HTTPException
from inference import SentimentModel

app = FastAPI()

# Ładowanie modeli przy starcie serwera
sentiment_model = SentimentModel()


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest) -> PredictResponse:
    if not request.text.strip():
        raise HTTPException(
            status_code=422, detail="Text must not be empty or whitespace only"
        )

    prediction = sentiment_model.predict(request.text)
    return PredictResponse(prediction=prediction)
