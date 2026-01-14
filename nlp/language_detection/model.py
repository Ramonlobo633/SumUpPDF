from dataclasses import dataclass

@dataclass
class LanguagePrediction:
    language: str
    confidence: float
    source: str