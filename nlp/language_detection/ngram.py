import joblib
from .base import LanguageDetector, LanguagePrediction

class ClassicalLanguageDetector(LanguageDetector):
    def __init__(self, model_path: str, vectorizer_path: str):
        self.model = joblib.load(model_path)
        self.vectorizer = joblib.load(vectorizer_path)
        self.name = "char-ngram-model"

    def detect(self, text: str) -> LanguagePrediction:
        if not text.strip():
            return LanguagePrediction("unknown", 0.0, self.name)

        X = self.vectorizer.transform([text])
        probs = self.model.predict_proba(X)[0]

        idx = probs.argmax()
        return LanguagePrediction(
            language=self.model.classes_[idx],
            confidence=float(probs[idx]),
            source=self.name
        )
