import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier


def load_data():
    return load_iris(return_X_y=True, as_frame=False)


def train_model():
    X, y = load_data()
    model = RandomForestClassifier(random_state=42)
    model.fit(X, y)
    return model


def save_model(model, filename: str = "model.joblib") -> None:
    joblib.dump(model, filename)


if __name__ == "__main__":
    trained_model = train_model()
    save_model(trained_model)
    print("Model trained and saved to model.joblib")
