from pathlib import Path
import joblib
from cleantext import clean
from sentence_transformers import SentenceTransformer


class SentimentModel:
    def __init__(self, model_dir: Path | str = "models/model"):
        model_dir = Path(model_dir)
        self.label_mapping = {0: "negative", 1: "neutral", 2: "positive"}
        transformer_path = model_dir / "sentence_transformer.model"
        self.transformer = SentenceTransformer(
            str(transformer_path), local_files_only=True
        )
        self.classifier = joblib.load(model_dir / "classifier.joblib")

    def clean_input(self, text: str) -> str:
        return clean(
            text,
            fix_unicode=True,
            to_ascii=True,
            lower=True,
            no_line_breaks=True,
            no_urls=True,
            no_emails=True,
            no_phone_numbers=True,
            no_numbers=False,
            no_digits=False,
            no_currency_symbols=False,
        )

    def predict(self, text: str) -> str:
        cleaned_text = self.clean_input(text)
        embeddings = self.transformer.encode([cleaned_text])
        prediction_id = self.classifier.predict(embeddings)[0]
        return self.label_mapping[int(prediction_id)]
