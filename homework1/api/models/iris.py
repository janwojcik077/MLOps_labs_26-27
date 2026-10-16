from pydantic import BaseModel, Field


class PredictRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Text cannot be empty")


class PredictResponse(BaseModel):
    prediction: str
