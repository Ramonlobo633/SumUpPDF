from unicode_detector import detect_script
from .base import LanguagePrediction

class LanguageDetectionService:
    def __init__(
        self,
        classical_detector,
        llm_detector=None,
        confidence_threshold=0.75
    ):
        self.classical = classical_detector
        self.llm = llm_detector
        self.threshold = confidence_threshold

    def detect(self, text: str) -> LanguagePrediction:
        script = detect_script(text)

        # Classical first
        result = self.classical.detect(text)

        if result.confidence >= self.threshold:
            return result

        # LLM fallback
        if self.llm:
            llm_result = self.llm.detect(text)
            return llm_result

        return result