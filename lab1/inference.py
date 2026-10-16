import joblib
from sklearn.datasets import load_iris


class ModelInference:
    def __init__(self, model_path: str = "model.joblib"):
        self.model = self.load_model(model_path)
        self.target_names = load_iris().target_names

    def load_model(self, model_path: str):
        return joblib.load(model_path)

    def predict(self, data: dict) -> str:
        features = [
            [
                data["sepal_length"],
                data["sepal_width"],
                data["petal_length"],
                data["petal_width"],
            ]
        ]
        prediction_index = self.model.predict(features)[0]
        return str(self.target_names[prediction_index])
