from fastapi import FastAPI
from api.models.iris import PredictRequest, PredictResponse
from inference import ModelInference

app = FastAPI()


model = ModelInference()


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest) -> PredictResponse:
    prediction = model.predict(request.model_dump())
    return PredictResponse(prediction=prediction)
