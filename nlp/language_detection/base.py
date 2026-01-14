from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class LanguagePrediction:
    language: str 
    confidence: float 
    source: str    

class LanguageDetector(ABC):
    @abstractmethod
    def detect(self, text: str) -> LanguagePrediction:
        pass
